# Kaggle Dataset Upload Information (UPDATED - Deduplicated Data)

## Basic Information

### Dataset Title

```
Polymarket Prediction Markets - Complete Dataset (44K Events)
```

### Subtitle

```
Clean prediction market data: 43,840 events, 100,795 markets, $8B volume, Dec 2025 snapshot
```

### Description (Markdown supported)

```markdown
# Polymarket Prediction Markets Dataset

Complete **deduplicated** dataset of prediction market events and individual markets from Polymarket, one of the world's largest decentralized prediction markets platforms.

## Dataset Overview

This dataset contains a comprehensive snapshot of Polymarket's marketplace as of **December 3, 2025**, including:

- **43,840 unique events** across politics, sports, crypto, and more
- **100,795 individual markets** with detailed trading data
- **$7.99B total trading volume** (all-time)
- **$150M daily volume** snapshot
- **$315M total liquidity**
- **2.3 years of historical data** (July 2022 - December 2025)

⚠️ **Data Quality Note:** This dataset has been **deduplicated and verified** to contain only unique records with zero duplicate IDs. Previous API calls caused 50% duplication, which has been corrected.

## What is Polymarket?

Polymarket is a decentralized prediction market platform where users bet on the outcomes of real-world events. Markets range from political elections to sports outcomes, cryptocurrency prices, and cultural predictions.

## Files Included

### 1. polymarket_events.csv (100 MB, 43,840 rows)
Event-level data with 67 columns including:
- Event metadata (id, title, slug, description)
- Trading metrics (volume, volume24hr, volume1wk, liquidity)
- Status flags (active, closed, featured, restricted)
- Timestamps (startDate, endDate, createdAt, updatedAt)
- Category tags (JSON format)
- Competitiveness scores
- Market counts per event

### 2. polymarket_markets.csv (202 MB, 100,795 rows)
Individual market data with 106 columns including:
- Market details (question, outcomes, outcomePrices)
- Trading activity (volume, liquidity, spread)
- Order book data (bestBid, bestAsk, acceptingOrders)
- Event references (event_id, event_slug, event_title)
- CLOB (Central Limit Order Book) data
- Token IDs and reward structures
- Resolution status and timestamps

## Key Statistics

- **Platform Lifespan:** July 2022 - Present
- **Total Volume (All-Time):** $7.99 Billion
- **24-Hour Volume:** $150.1 Million
- **Total Liquidity:** $315.1 Million
- **Average Markets per Event:** 2.3
- **Events Created (Last 30 Days):** 23,923 (55% of all events)
- **Most Active Category:** Crypto (24,874 events)
- **Data Quality:** 100% unique records, zero duplicates

## Data Collection & Processing

- **Source:** Polymarket Gamma API (https://gamma-api.polymarket.com/public-search)
- **Method:** Asynchronous pagination using Python aiohttp
- **Pages Fetched:** 2,192 complete pages
- **Collection Date:** December 3, 2025
- **Data Loss:** Zero - all nested structures preserved as JSON strings
- **Deduplication:** Applied to remove 50% API-caused duplicates
- **Verification:** All IDs verified unique, integrity checked

## Use Cases

This dataset is ideal for:

1. **Market Analysis:** Study prediction market dynamics and efficiency
2. **Behavioral Economics:** Analyze crowd wisdom and betting patterns
3. **Machine Learning:** Train models on market outcomes and prices
4. **Financial Research:** Study liquidity, volume, and price discovery
5. **Time Series Analysis:** Track event creation and market trends
6. **Network Analysis:** Study market relationships and competitiveness
7. **Sentiment Analysis:** Correlation between predictions and real outcomes
8. **Algorithmic Trading:** Develop and backtest prediction market strategies

## Data Quality

- ✅ Complete pagination (all 2,192 pages)
- ✅ Zero data loss (nested arrays/objects preserved as JSON)
- ✅ **100% unique records** (deduplicated by ID)
- ✅ 67 event fields captured (including dynamic fields)
- ✅ 106 market fields captured (complete market microstructure)
- ✅ All timestamps in ISO 8601 format
- ✅ Numeric fields properly formatted
- ✅ Verified data integrity (no duplicate IDs)

## Sample Insights

- **55% of all events** created in the last 30 days (explosive growth)
- **Fed decision event** leads with $14.96M in 24h volume
- **Strong correlation** between liquidity and trading volume (r > 0.8)
- **Binary markets dominate** with most events having 1-2 outcome markets
- **Crypto markets** represent over 50% of all events
- **Average 797 events/day** creation rate (last 30 days)

## Data Format

- **File Format:** CSV (UTF-8 encoded)
- **Nested Structures:** JSON-encoded strings (parse with `json.loads()` in Python)
- **Missing Values:** Empty strings or null
- **Boolean Values:** "True"/"False" strings
- **Numeric Values:** Float format with full precision
- **Duplicates:** None (verified unique by ID)

## Usage Examples

### Python
```python
import pandas as pd
import json

# Load data
events = pd.read_csv('polymarket_events.csv')
markets = pd.read_csv('polymarket_markets.csv')

# Verify no duplicates
print(f"Events: {len(events)} rows, {events['id'].nunique()} unique IDs")
print(f"Markets: {len(markets)} rows, {markets['id'].nunique()} unique IDs")

# Parse nested JSON
events['tags_parsed'] = events['tags'].apply(
    lambda x: json.loads(x) if pd.notna(x) else []
)

# Analyze volume
print(f"Total Volume: ${events['volume'].sum()/1e9:.2f}B")
print(f"Top Event: {events.nlargest(1, 'volume24hr')['title'].values[0]}")

# Market analysis
markets['outcomes_parsed'] = markets['outcomes'].apply(json.loads)
print(f"Average markets per event: {len(markets) / len(events):.2f}")
```

### R

```r
library(tidyverse)
library(jsonlite)

# Load data
events <- read_csv('polymarket_events.csv')
markets <- read_csv('polymarket_markets.csv')

# Verify no duplicates
cat(sprintf("Events: %d unique out of %d rows\n",
    n_distinct(events$id), nrow(events)))

# Parse JSON fields
events$tags_parsed <- lapply(events$tags, fromJSON)
markets$outcomes_parsed <- lapply(markets$outcomes, fromJSON)

# Summary statistics
summary(events$volume24hr)
```

## Related Links

- **GitHub Repository:** [Analysis Code &amp; Visualizations](https://github.com/[your-username]/polymarket_com)
- **Polymarket Platform:** https://polymarket.com
- **API Documentation:** Gamma API public search endpoint

## Version History

**v1.1 (Current)** - December 3, 2025

- ✅ Deduplicated dataset (removed 50% API-caused duplicates)
- ✅ Verified all unique IDs
- ✅ Updated all statistics
- 43,840 unique events, 100,795 unique markets

**v1.0** - December 3, 2025 (Initial)

- Had duplicate records due to API preset configuration
- Superseded by v1.1

## Citation

If you use this dataset in your research, please cite:

```
Polymarket Prediction Markets Dataset (2025)
Collected from Polymarket Gamma API
Dataset available at: https://www.kaggle.com/datasets/ismetsemedov/polymarket
Collection Date: December 3, 2025
Version: 1.1 (Deduplicated)
```

## License

This dataset is provided for research and educational purposes. Data sourced from Polymarket's public API. Please review Polymarket's Terms of Service for commercial use restrictions.

## Updates

This is a point-in-time snapshot from December 3, 2025. The dataset has been deduplicated and verified for data quality. For real-time data, use the provided fetch script from the GitHub repository or query the Polymarket API directly.

## Tags

prediction-markets, polymarket, decentralized-finance, defi, blockchain, cryptocurrency, politics, sports-betting, market-data, financial-data, time-series, trading-volume, liquidity, economics, behavioral-economics, clean-data, deduplicated

```

---

## Tags/Keywords (Select all that apply)

**Primary Tags:**
- Finance
- Business
- Economics
- Time Series
- Cryptocurrency

**Additional Tags (type in search box):**
- prediction markets
- polymarket
- blockchain
- defi
- decentralized finance
- trading
- market data
- betting
- political predictions
- sports betting
- liquidity
- volume
- market microstructure
- crowd wisdom
- forecasting
- clean data
- deduplicated

---

## License

**Recommended:** `Database: Open Database (ODbL)`

**Why:** This license allows sharing, modifying, and using the database while requiring attribution. It's commonly used for data extracted from public APIs.

**Alternative:** `CC0: Public Domain` if you want no restrictions

---

## Visibility

**Public** ✅ (Recommended so others can use it)

---

## File Descriptions

### polymarket_events.csv
```

Event-level prediction market data with 43,840 unique events. Contains trading volume, liquidity, status, timestamps, categories, and market counts. Deduplicated and verified for data quality. All events from Polymarket platform (July 2022 - December 2025).

```

### polymarket_markets.csv
```

Market-level data with 100,795 unique prediction markets. Includes questions, outcomes, prices, order book data, trading activity, and resolution status. Links to parent events via event_id. Deduplicated dataset with zero duplicate records.

```

---

## Usability Rating

Aim for **10.0** by ensuring:
- ✅ Clear column names
- ✅ Comprehensive description
- ✅ Sample code provided
- ✅ Data quality documented and verified
- ✅ Use cases explained
- ✅ Citation format included
- ✅ Deduplication process explained
- ✅ Version history provided

---

## Collaborators (Optional)

You can add collaborators later if needed.

---

## Additional Metadata (Optional but Recommended)

### Update Frequency
```

Static Snapshot (December 3, 2025) - Version 1.1 (Deduplicated)

```

### Expected Update Cadence
```

Irregular - New snapshots may be uploaded periodically

```

### Data Source
```

Polymarket Gamma API (https://gamma-api.polymarket.com)

```

### Collection Method
```

Automated collection using Python async requests (aiohttp) with complete pagination across 2,192 API pages. Data deduplicated to remove API-caused duplicates and verified for uniqueness.

```

### Data Quality
```

Version 1.1: Deduplicated dataset with 100% unique records verified by ID. Zero duplicate entries. All nested structures preserved as JSON. Complete data integrity verified.

```

---

## Cover Image (Optional but Recommended)

**Suggestion:** Upload one of your generated charts as the cover image.

**Best options:**
1. `charts/03_volume_metrics.png` - Shows key metrics ($8B volume, $150M daily)
2. `charts/01_top_events_volume.png` - Shows top events
3. `charts/07_liquidity_vs_volume.png` - Shows correlation scatter plot

This makes your dataset more visually appealing and increases discoverability.

---

## Tips for Maximum Visibility

1. **Use all relevant tags** - Include "clean-data" and "deduplicated"
2. **Add cover image** - Datasets with images get more views
3. **Include sample code** - Makes dataset more accessible
4. **Link to GitHub** - Shows complete analysis
5. **Mention data quality** - Highlight deduplication in title/subtitle
6. **Respond to comments** - Build community engagement
7. **Write a kernel/notebook** - Create analysis notebook on Kaggle using your data
8. **Update description** - Clearly state this is the clean, deduplicated version

---

## Quick Checklist Before Upload

- [ ] CSV files are under 20GB (✓ You're at 302MB)
- [ ] Files are UTF-8 encoded (✓)
- [ ] No sensitive data included (✓)
- [ ] **No duplicate records** (✓ Verified)
- [ ] Description is clear and comprehensive (✓)
- [ ] Tags are relevant (✓)
- [ ] License is selected (Choose ODbL)
- [ ] Files have descriptions (✓)
- [ ] Cover image uploaded (Optional)
- [ ] Sample code provided (✓)
- [ ] **Data quality mentioned prominently** (✓)

---

## Post-Upload Steps

1. **Create a Notebook** on Kaggle using your dataset
2. **Update GitHub README** with final Kaggle URL
3. **Share on social media** with #Polymarket #DataScience #CleanData
4. **Monitor discussions** and answer questions
5. **Consider updating** the dataset monthly or quarterly
6. **Pin a comment** explaining the deduplication process

---

## Example Social Media Post

```

🚀 Just published a CLEAN Polymarket dataset on Kaggle!

📊 43,840 unique prediction market events (deduplicated!)
💰 $8B in trading volume
📈 100,795 individual markets
🗓️ 2.3 years of historical data
✅ 100% unique records - zero duplicates

Perfect for ML, economics research, and market analysis!

Key stats:
• $150M daily volume
• $315M liquidity
• 55% of events created in last 30 days
• 24K crypto-related events

🔗 https://www.kaggle.com/datasets/ismetsemedov/polymarket

#DataScience #PredictionMarkets #Polymarket #MachineLearning #DeFi #CleanData

```

---

## Important Update Note for Description

**Add this prominent callout at the top of your description:**

```markdown
## ⚠️ Data Quality Update

**Version 1.1 (Current):** This dataset has been **deduplicated and verified** to ensure data quality. The original API configuration caused 50% duplication (each record appeared twice). This version contains only unique records:

- ✅ **43,840 unique events** (was 87,680 with duplicates)
- ✅ **100,795 unique markets** (was 201,590 with duplicates)
- ✅ **Zero duplicate IDs** - fully verified
- ✅ **All statistics adjusted** to reflect true values

All metrics in this dataset represent actual trading activity without inflation from duplicates.
```

This transparency will build trust with users and demonstrate your commitment to data quality.
