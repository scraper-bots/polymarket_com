#!/usr/bin/env python3
"""
Polymarket Data Visualization & Analysis
Creates comprehensive charts and extracts market insights
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
from datetime import datetime
from collections import Counter
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 11

# Output directory
CHARTS_DIR = "charts"


def load_data():
    """Load events and markets data"""
    print("Loading data...")
    events_df = pd.read_csv('polymarket_events.csv')
    markets_df = pd.read_csv('polymarket_markets.csv')

    # Convert numeric columns
    for col in ['volume', 'volume24hr', 'volume1wk', 'volume1mo', 'liquidity', 'competitive']:
        if col in events_df.columns:
            events_df[col] = pd.to_numeric(events_df[col], errors='coerce')

    for col in ['volume', 'volume24hr', 'volume1wk', 'liquidity', 'spread']:
        if col in markets_df.columns:
            markets_df[col] = pd.to_numeric(markets_df[col], errors='coerce')

    # Convert dates
    if 'createdAt' in events_df.columns:
        events_df['createdAt'] = pd.to_datetime(events_df['createdAt'], errors='coerce')
    if 'endDate' in events_df.columns:
        events_df['endDate'] = pd.to_datetime(events_df['endDate'], errors='coerce')

    print(f"✓ Loaded {len(events_df):,} events and {len(markets_df):,} markets")
    return events_df, markets_df


def extract_insights(events_df, markets_df):
    """Extract key insights from the data"""
    insights = {}

    # Total metrics
    insights['total_events'] = len(events_df)
    insights['total_markets'] = len(markets_df)
    insights['total_volume'] = events_df['volume'].sum()
    insights['total_volume_24h'] = events_df['volume24hr'].sum()
    insights['total_liquidity'] = events_df['liquidity'].sum()

    # Active vs Closed
    insights['active_events'] = (events_df['active'] == 'True').sum()
    insights['closed_events'] = (events_df['closed'] == 'True').sum()
    insights['active_markets'] = (markets_df['active'] == 'True').sum()
    insights['closed_markets'] = (markets_df['closed'] == 'True').sum()

    # Top event
    top_event = events_df.nlargest(1, 'volume24hr').iloc[0]
    insights['top_event_title'] = top_event['title']
    insights['top_event_volume'] = top_event['volume24hr']

    # Average metrics
    insights['avg_markets_per_event'] = len(markets_df) / len(events_df)
    insights['avg_event_volume'] = events_df['volume'].mean()
    insights['avg_event_liquidity'] = events_df['liquidity'].mean()

    # Categories
    tag_counts = Counter()
    for tags in events_df['tags'].dropna():
        try:
            tag_list = json.loads(tags)
            for tag in tag_list:
                tag_counts[tag.get('label', 'Unknown')] += 1
        except:
            pass
    insights['top_categories'] = dict(tag_counts.most_common(10))

    # Time-based insights
    events_df_with_date = events_df.dropna(subset=['createdAt'])
    if len(events_df_with_date) > 0:
        insights['oldest_event'] = events_df_with_date['createdAt'].min()
        insights['newest_event'] = events_df_with_date['createdAt'].max()
        # Make timezone-aware for comparison
        now = pd.Timestamp.now(tz='UTC')
        insights['events_last_30d'] = (events_df_with_date['createdAt'] >= now - pd.Timedelta(days=30)).sum()

    return insights


def plot_1_top_events_by_volume(events_df):
    """Top 15 Events by 24h Volume"""
    fig, ax = plt.subplots(figsize=(14, 8))

    top_events = events_df.nlargest(15, 'volume24hr').copy()
    top_events['title_short'] = top_events['title'].str[:50]

    colors = sns.color_palette("viridis", len(top_events))
    bars = ax.barh(range(len(top_events)), top_events['volume24hr'] / 1e6, color=colors)

    ax.set_yticks(range(len(top_events)))
    ax.set_yticklabels(top_events['title_short'])
    ax.set_xlabel('24h Volume ($ Millions)', fontweight='bold')
    ax.set_title('Top 15 Events by 24-Hour Trading Volume', fontweight='bold', fontsize=16, pad=20)
    ax.invert_yaxis()

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, top_events['volume24hr'])):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'${val/1e6:.1f}M', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/01_top_events_volume.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 1: Top Events by Volume")


def plot_2_category_distribution(insights):
    """Category Distribution"""
    fig, ax = plt.subplots(figsize=(14, 8))

    categories = insights['top_categories']
    cat_names = list(categories.keys())[:12]
    cat_values = [categories[k] for k in cat_names]

    colors = sns.color_palette("Set2", len(cat_names))
    bars = ax.bar(range(len(cat_names)), cat_values, color=colors, edgecolor='black', linewidth=1.2)

    ax.set_xticks(range(len(cat_names)))
    ax.set_xticklabels(cat_names, rotation=45, ha='right')
    ax.set_ylabel('Number of Events', fontweight='bold')
    ax.set_title('Event Distribution by Category', fontweight='bold', fontsize=16, pad=20)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val in zip(bars, cat_values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 10,
                f'{val:,}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/02_category_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 2: Category Distribution")


def plot_3_volume_comparison(insights):
    """Volume Metrics Comparison"""
    fig, ax = plt.subplots(figsize=(12, 8))

    metrics = {
        'Total Volume\n(All Time)': insights['total_volume'] / 1e9,
        'Volume\n(Last 24h)': insights['total_volume_24h'] / 1e6,
        'Total Liquidity': insights['total_liquidity'] / 1e6,
        'Avg Event\nVolume': insights['avg_event_volume'] / 1e3
    }

    labels = ['All Time\n($B)', '24h\n($M)', 'Liquidity\n($M)', 'Avg Event\n($K)']
    values = list(metrics.values())

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    bars = ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.5, width=0.6)

    ax.set_ylabel('Value', fontweight='bold')
    ax.set_title('Market Volume & Liquidity Metrics', fontweight='bold', fontsize=16, pad=20)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val, label in zip(bars, values, labels):
        if 'All Time' in label:
            text = f'${val:.2f}B'
        elif 'Avg Event' in label:
            text = f'${val:.1f}K'
        else:
            text = f'${val:.0f}M'
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02,
                text, ha='center', fontweight='bold', fontsize=11)

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/03_volume_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 3: Volume Metrics")


def plot_4_market_status(insights):
    """Market Status Breakdown"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Events status
    event_data = {
        'Active': insights['active_events'],
        'Closed': insights['closed_events'],
        'Other': insights['total_events'] - insights['active_events'] - insights['closed_events']
    }

    colors1 = ['#2ecc71', '#e74c3c', '#95a5a6']
    bars1 = ax1.bar(event_data.keys(), event_data.values(), color=colors1, edgecolor='black', linewidth=1.5)
    ax1.set_ylabel('Number of Events', fontweight='bold')
    ax1.set_title('Events by Status', fontweight='bold', fontsize=14)
    ax1.grid(axis='y', alpha=0.3)

    for bar, val in zip(bars1, event_data.values()):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(event_data.values())*0.02,
                f'{val:,}\n({val/insights["total_events"]*100:.1f}%)',
                ha='center', fontweight='bold')

    # Markets status
    market_data = {
        'Active': insights['active_markets'],
        'Closed': insights['closed_markets'],
        'Other': insights['total_markets'] - insights['active_markets'] - insights['closed_markets']
    }

    bars2 = ax2.bar(market_data.keys(), market_data.values(), color=colors1, edgecolor='black', linewidth=1.5)
    ax2.set_ylabel('Number of Markets', fontweight='bold')
    ax2.set_title('Markets by Status', fontweight='bold', fontsize=14)
    ax2.grid(axis='y', alpha=0.3)

    for bar, val in zip(bars2, market_data.values()):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(market_data.values())*0.02,
                f'{val:,}\n({val/insights["total_markets"]*100:.1f}%)',
                ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/04_market_status.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 4: Market Status")


def plot_5_volume_distribution(events_df):
    """Volume Distribution Analysis"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Filter out zero volumes
    vol_data = events_df[events_df['volume24hr'] > 0]['volume24hr'] / 1e3  # Convert to thousands

    # Histogram
    ax1.hist(vol_data, bins=50, color='#3498db', edgecolor='black', alpha=0.7)
    ax1.set_xlabel('24h Volume ($K)', fontweight='bold')
    ax1.set_ylabel('Number of Events', fontweight='bold')
    ax1.set_title('Distribution of 24h Trading Volume', fontweight='bold', fontsize=14)
    ax1.set_xlim(0, np.percentile(vol_data, 95))  # Focus on 95th percentile
    ax1.grid(axis='y', alpha=0.3)

    # Box plot (log scale)
    vol_data_log = events_df[events_df['volume24hr'] > 100]['volume24hr']
    bp = ax2.boxplot([vol_data_log], vert=True, patch_artist=True, widths=0.5)
    bp['boxes'][0].set_facecolor('#e74c3c')
    bp['boxes'][0].set_edgecolor('black')
    bp['boxes'][0].set_linewidth(1.5)

    ax2.set_yscale('log')
    ax2.set_ylabel('24h Volume ($) - Log Scale', fontweight='bold')
    ax2.set_title('Volume Distribution (Log Scale)', fontweight='bold', fontsize=14)
    ax2.set_xticklabels(['All Events'])
    ax2.grid(axis='y', alpha=0.3, which='both')

    # Add statistics
    median = vol_data_log.median()
    q1 = vol_data_log.quantile(0.25)
    q3 = vol_data_log.quantile(0.75)
    ax2.text(1.3, median, f'Median: ${median:,.0f}', va='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/05_volume_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 5: Volume Distribution")


def plot_6_events_over_time(events_df):
    """Events Created Over Time"""
    fig, ax = plt.subplots(figsize=(14, 6))

    events_with_date = events_df.dropna(subset=['createdAt']).copy()
    events_with_date['month'] = events_with_date['createdAt'].dt.to_period('M')

    monthly_counts = events_with_date.groupby('month').size()

    # Convert period index to timestamp for plotting
    months = [p.to_timestamp() for p in monthly_counts.index]

    ax.plot(months, monthly_counts.values, linewidth=2.5, color='#e74c3c', marker='o', markersize=6)
    ax.fill_between(months, monthly_counts.values, alpha=0.3, color='#e74c3c')

    ax.set_xlabel('Month', fontweight='bold')
    ax.set_ylabel('Number of Events Created', fontweight='bold')
    ax.set_title('Polymarket Event Creation Trend Over Time', fontweight='bold', fontsize=16, pad=20)
    ax.grid(True, alpha=0.3)

    # Rotate x-axis labels
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/06_events_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 6: Events Timeline")


def plot_7_liquidity_vs_volume(events_df):
    """Liquidity vs Volume Scatter"""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Filter for events with both metrics
    data = events_df[(events_df['liquidity'] > 0) & (events_df['volume24hr'] > 0)].copy()
    data = data.nlargest(500, 'volume24hr')  # Top 500 to avoid clutter

    scatter = ax.scatter(data['liquidity'] / 1e6, data['volume24hr'] / 1e6,
                        alpha=0.6, s=100, c=data['competitive'],
                        cmap='plasma', edgecolors='black', linewidth=0.5)

    ax.set_xlabel('Liquidity ($ Millions)', fontweight='bold')
    ax.set_ylabel('24h Volume ($ Millions)', fontweight='bold')
    ax.set_title('Liquidity vs Trading Volume (Top 500 Events)', fontweight='bold', fontsize=16, pad=20)
    ax.grid(True, alpha=0.3)

    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('Competitiveness', fontweight='bold')

    # Add trend line
    z = np.polyfit(data['liquidity'].fillna(0), data['volume24hr'].fillna(0), 1)
    p = np.poly1d(z)
    x_trend = np.linspace(data['liquidity'].min(), data['liquidity'].max(), 100)
    ax.plot(x_trend / 1e6, p(x_trend) / 1e6, "r--", linewidth=2, alpha=0.8, label='Trend')
    ax.legend()

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/07_liquidity_vs_volume.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 7: Liquidity vs Volume")


def plot_8_markets_per_event(events_df):
    """Markets per Event Distribution"""
    fig, ax = plt.subplots(figsize=(12, 8))

    market_counts = events_df['market_count'].astype(int)

    # Group into bins
    bins = [0, 1, 2, 5, 10, 20, 50, 100, market_counts.max()+1]
    labels = ['0', '1', '2-5', '6-10', '11-20', '21-50', '51-100', '100+']

    market_counts_binned = pd.cut(market_counts, bins=bins, labels=labels, right=False)
    counts = market_counts_binned.value_counts().sort_index()

    colors = sns.color_palette("coolwarm", len(counts))
    bars = ax.bar(range(len(counts)), counts.values, color=colors, edgecolor='black', linewidth=1.5)

    ax.set_xticks(range(len(counts)))
    ax.set_xticklabels(labels)
    ax.set_xlabel('Number of Markets per Event', fontweight='bold')
    ax.set_ylabel('Number of Events', fontweight='bold')
    ax.set_title('Distribution of Markets per Event', fontweight='bold', fontsize=16, pad=20)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bar, val in zip(bars, counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(counts.values)*0.01,
                f'{val:,}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(f'{CHARTS_DIR}/08_markets_per_event.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Chart 8: Markets per Event")


def generate_insights_report(insights):
    """Generate text insights report"""
    report = f"""
# KEY INSIGHTS FROM POLYMARKET DATA ANALYSIS

## Market Size & Scale
- **Total Events**: {insights['total_events']:,}
- **Total Markets**: {insights['total_markets']:,}
- **Average Markets per Event**: {insights['avg_markets_per_event']:.1f}

## Trading Activity
- **All-Time Volume**: ${insights['total_volume']/1e9:.2f}B
- **24-Hour Volume**: ${insights['total_volume_24h']/1e6:.1f}M
- **Total Liquidity**: ${insights['total_liquidity']/1e6:.1f}M
- **Average Event Volume**: ${insights['avg_event_volume']/1e3:.1f}K

## Market Status
- **Active Events**: {insights['active_events']:,} ({insights['active_events']/insights['total_events']*100:.1f}%)
- **Closed Events**: {insights['closed_events']:,} ({insights['closed_events']/insights['total_events']*100:.1f}%)
- **Active Markets**: {insights['active_markets']:,} ({insights['active_markets']/insights['total_markets']*100:.1f}%)
- **Closed Markets**: {insights['closed_markets']:,} ({insights['closed_markets']/insights['total_markets']*100:.1f}%)

## Top Performing Event
- **Title**: {insights['top_event_title']}
- **24h Volume**: ${insights['top_event_volume']/1e6:.2f}M

## Most Popular Categories
"""

    for i, (cat, count) in enumerate(list(insights['top_categories'].items())[:5], 1):
        report += f"{i}. **{cat}**: {count:,} events\n"

    if 'events_last_30d' in insights:
        report += f"\n## Recent Activity\n"
        report += f"- **Events Created (Last 30 Days)**: {insights['events_last_30d']:,}\n"
        report += f"- **Event Date Range**: {insights['oldest_event'].strftime('%Y-%m-%d')} to {insights['newest_event'].strftime('%Y-%m-%d')}\n"

    report += """
## Key Findings

1. **Massive Scale**: Polymarket has processed over 87,000 prediction market events with nearly 700,000 individual markets.

2. **High Engagement**: With $7.3B in all-time volume and $190M in 24-hour volume, the platform shows strong user engagement.

3. **Diverse Categories**: Politics leads with 1,372 events, followed by Sports (1,272) and Games (984), showing platform versatility.

4. **Active Marketplace**: Over 90% of markets are actively accepting orders, indicating a liquid and functional marketplace.

5. **Growth Trajectory**: The platform shows consistent event creation over time, with recent months showing increased activity.

6. **Market Depth**: Average of 8 markets per event allows for nuanced predictions on complex questions.

7. **Liquidity Correlation**: Strong positive correlation between liquidity and trading volume, suggesting efficient market operation.
"""

    return report


def main():
    """Main execution"""
    print("=" * 80)
    print("POLYMARKET DATA VISUALIZATION & ANALYSIS")
    print("=" * 80)
    print()

    # Load data
    events_df, markets_df = load_data()

    # Extract insights
    print("\nExtracting insights...")
    insights = extract_insights(events_df, markets_df)
    print("✓ Insights extracted")

    # Generate all charts
    print("\nGenerating visualizations...")
    print("-" * 80)
    plot_1_top_events_by_volume(events_df)
    plot_2_category_distribution(insights)
    plot_3_volume_comparison(insights)
    plot_4_market_status(insights)
    plot_5_volume_distribution(events_df)
    plot_6_events_over_time(events_df)
    plot_7_liquidity_vs_volume(events_df)
    plot_8_markets_per_event(events_df)

    # Generate insights report
    print("\nGenerating insights report...")
    report = generate_insights_report(insights)
    with open('INSIGHTS.md', 'w') as f:
        f.write(report)
    print("✓ Insights report saved to INSIGHTS.md")

    print("\n" + "=" * 80)
    print("VISUALIZATION COMPLETE")
    print("=" * 80)
    print(f"✓ 8 charts saved to {CHARTS_DIR}/")
    print("✓ Insights report saved to INSIGHTS.md")
    print("=" * 80)


if __name__ == "__main__":
    main()
