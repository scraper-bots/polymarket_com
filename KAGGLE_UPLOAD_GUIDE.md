# Kaggle Upload Step-by-Step Guide

## Section 1: Basic Information Tab

### 1. Add Tags
Click "Add tags" and type these one by one:

```
prediction-markets
polymarket
blockchain
defi
cryptocurrency
trading
market-data
clean-data
deduplicated
time-series
liquidity
volume
economics
forecasting
```

Then select from categories:
- Finance ✅
- Business ✅
- Economics ✅
- Time Series ✅
- Cryptocurrency ✅

---

### 2. Add Description (About Dataset)

Copy the entire description from `KAGGLE_DATASET_INFO.md` starting from:

```markdown
# Polymarket Prediction Markets Dataset

Complete **deduplicated** dataset of prediction market events...
```

**Important:** Start with the quality warning at the top:

```markdown
## ⚠️ Data Quality Update

**Version 1.1 (Current):** This dataset has been **deduplicated and verified**...
```

---

## Section 2: File Information Tab

### For polymarket_events.csv:

**File Description:**
```
Event-level prediction market data with 43,840 unique events. Contains trading volume, liquidity, status, timestamps, categories, and market counts. Deduplicated and verified for data quality. All events from Polymarket platform (July 2022 - December 2025).
```

### For polymarket_markets.csv:

**File Description:**
```
Market-level data with 100,795 unique prediction markets. Includes questions, outcomes, prices, order book data, trading activity, and resolution status. Links to parent events via event_id. Deduplicated dataset with zero duplicate records.
```

---

## Section 3: Column Descriptors Tab

### For polymarket_events.csv

Click on the file, then "Add column descriptions". You'll see 67 columns. Here are the most important ones to describe:

**Quick Entry Format:**
Column Name | Description

Copy-paste these (Kaggle usually has a bulk import option):

```
id | Unique event identifier
title | Full event title/question
description | Detailed event description with resolution criteria
volume | Total all-time trading volume in USD
volume24hr | Trading volume in last 24 hours in USD
liquidity | Total liquidity available in USD
active | Whether event is currently active (True/False)
closed | Whether event has closed (True/False)
startDate | Event start date (ISO 8601 datetime)
endDate | Event end date (ISO 8601 datetime)
tags | JSON array of category tags with metadata
market_count | Number of markets within this event
competitive | Competitiveness score between 0-1
```

For complete list, see `COLUMN_DESCRIPTIONS.md`

---

### For polymarket_markets.csv

**Quick Entry Format:**

```
id | Unique market identifier
event_id | Parent event ID (foreign key)
question | Market question/proposition
outcomes | JSON array of possible outcomes (e.g., ["Yes", "No"])
outcomePrices | JSON array of current prices 0-1
volume | Total all-time volume in USD
volume24hr | Volume in last 24 hours in USD
liquidity | Total liquidity in USD
bestBid | Best bid price in order book
bestAsk | Best ask price in order book
spread | Bid-ask spread
active | Whether market is active (True/False)
closed | Whether market is closed (True/False)
acceptingOrders | Currently accepting orders (True/False)
```

For complete list (106 columns), see `COLUMN_DESCRIPTIONS.md`

---

## Section 4: Metadata Tab

### Provenance (How data was collected)

```
Data Source: Polymarket Gamma API (https://gamma-api.polymarket.com/public-search)

Collection Method: Automated collection using Python async requests (aiohttp) with complete pagination across 2,192 API pages.

Processing: Data deduplicated to remove 50% API-caused duplicates (from dual preset configuration) and verified for uniqueness by ID field.

Date Collected: December 3, 2025

Data Quality: Version 1.1 - Deduplicated dataset with 100% unique records verified. Zero duplicate entries. All nested structures preserved as JSON strings. Complete data integrity verified.
```

---

### Update Frequency

```
Static Snapshot (December 3, 2025) - Version 1.1 (Deduplicated)

Expected Cadence: Irregular - New snapshots may be uploaded periodically (monthly or quarterly)
```

---

### License

Select: **Database: Open Database (ODbL)**

---

## Section 5: Cover Image (Optional but Recommended)

Upload one of these charts as thumbnail:

**Best option:**
- `charts/03_volume_metrics.png` - Shows $8B volume, clean stats

**Alternatives:**
- `charts/01_top_events_volume.png` - Top events
- `charts/07_liquidity_vs_volume.png` - Correlation chart

---

## Section 6: After Upload - Publish a Notebook

To boost usability to 10/10, create a Kaggle notebook using your data:

### Sample Notebook Structure:

```python
# Title: Polymarket Data Analysis - Quick Start

## Introduction
"""
This notebook demonstrates basic analysis of the Polymarket prediction
markets dataset. The data has been deduplicated and verified for quality.
"""

## Load Data
import pandas as pd
import json
import matplotlib.pyplot as plt

events = pd.read_csv('../input/polymarket/polymarket_events.csv')
markets = pd.read_csv('../input/polymarket/polymarket_markets.csv')

## Verify Data Quality
print(f"Events: {len(events):,} rows, {events['id'].nunique():,} unique")
print(f"Markets: {len(markets):,} rows, {markets['id'].nunique():,} unique")

## Basic Statistics
print(f"Total Volume: ${events['volume'].sum()/1e9:.2f}B")
print(f"24h Volume: ${events['volume24hr'].sum()/1e6:.1f}M")
print(f"Total Liquidity: ${events['liquidity'].sum()/1e6:.1f}M")

## Top Events
top_10 = events.nlargest(10, 'volume24hr')[['title', 'volume24hr', 'liquidity']]
print(top_10)

## Parse JSON Fields
events['tags_parsed'] = events['tags'].apply(
    lambda x: json.loads(x) if pd.notna(x) else []
)

## Category Distribution
from collections import Counter
all_tags = []
for tags in events['tags_parsed']:
    all_tags.extend([tag['label'] for tag in tags])

tag_counts = Counter(all_tags).most_common(10)
print("Top Categories:", tag_counts)

## Visualization
plt.figure(figsize=(12, 6))
events['volume24hr'].hist(bins=50)
plt.xlabel('24h Volume ($)')
plt.ylabel('Number of Events')
plt.title('Distribution of 24-Hour Trading Volume')
plt.show()
```

---

## Checklist Before Publishing

- [ ] Tags added (at least 10)
- [ ] Full description added with quality warning
- [ ] File descriptions added for both CSV files
- [ ] Key column descriptors added (at least top 10-15 per file)
- [ ] Provenance specified in metadata
- [ ] Update frequency specified
- [ ] License selected (ODbL)
- [ ] Cover image uploaded
- [ ] Dataset visibility set to Public
- [ ] Notebook published (optional but highly recommended)

---

## Expected Usability Score Breakdown

After completing all fields:

- **Documentation**: 10/10 (description, file info, columns)
- **Provenance**: 10/10 (source, method, dates)
- **Maintenance**: 8/10 (update frequency specified)
- **Examples**: 10/10 (if notebook published)

**Final Score: 9-10/10** ✅

---

## Quick Tips

1. **Use bulk import** for column descriptions if Kaggle supports it
2. **Link to GitHub** in description for code samples
3. **Mention "deduplicated"** prominently everywhere
4. **Add version note** (v1.1) to show quality improvement
5. **Publish notebook within 24h** for maximum impact
6. **Pin a comment** explaining the deduplication process
7. **Monitor questions** and respond quickly

---

## After Publishing

1. Get the final Kaggle URL
2. Update GitHub README with Kaggle link
3. Share on social media using provided template
4. Consider creating a blog post about the dataset
5. Monitor downloads and engagement
6. Respond to comments and questions
7. Plan next update (monthly/quarterly)

---

## Support

If you need help with any field:
- Check `COLUMN_DESCRIPTIONS.md` for complete column list
- Check `KAGGLE_DATASET_INFO.md` for all field templates
- Kaggle docs: https://www.kaggle.com/docs/datasets
