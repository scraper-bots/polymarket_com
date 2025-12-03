# Kaggle Dataset Upload Information

## Basic Information

### Dataset Title
```
Polymarket Prediction Markets - Complete Dataset (87K Events)
```

### Subtitle
```
Comprehensive prediction market data: 87,680 events, 201,590 markets, $16B volume, Dec 2025 snapshot
```

### Description (Markdown supported)

```markdown
# Polymarket Prediction Markets Dataset

Complete dataset of prediction market events and individual markets from Polymarket, one of the world's largest decentralized prediction markets platforms.

## Dataset Overview

This dataset contains a comprehensive snapshot of Polymarket's marketplace as of **December 3, 2025**, including:

- **87,680 events** across politics, sports, crypto, and more
- **201,590 individual markets** with detailed trading data
- **$15.98B total trading volume** (all-time)
- **$300M daily volume** snapshot
- **$630M total liquidity**
- **2.3 years of historical data** (July 2022 - December 2025)

## What is Polymarket?

Polymarket is a decentralized prediction market platform where users bet on the outcomes of real-world events. Markets range from political elections to sports outcomes, cryptocurrency prices, and cultural predictions.

## Files Included

### 1. polymarket_events.csv (200 MB, 87,680 rows)
Event-level data with 67 columns including:
- Event metadata (id, title, slug, description)
- Trading metrics (volume, volume24hr, volume1wk, liquidity)
- Status flags (active, closed, featured, restricted)
- Timestamps (startDate, endDate, createdAt, updatedAt)
- Category tags (JSON format)
- Competitiveness scores
- Market counts per event

### 2. polymarket_markets.csv (400 MB, 201,590 rows)
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
- **Total Volume (All-Time):** $15.98 Billion
- **24-Hour Volume:** $300.1 Million
- **Total Liquidity:** $630.2 Million
- **Average Markets per Event:** 2.3
- **Events Created (Last 30 Days):** 48,660
- **Most Active Category:** Crypto (49,748 events)

## Data Collection

- **Source:** Polymarket Gamma API (https://gamma-api.polymarket.com/public-search)
- **Method:** Asynchronous pagination using Python aiohttp
- **Pages Fetched:** 2,192 complete pages
- **Collection Date:** December 3, 2025
- **Data Loss:** Zero - all nested structures preserved as JSON strings

## Use Cases

This dataset is ideal for:

1. **Market Analysis:** Study prediction market dynamics and efficiency
2. **Behavioral Economics:** Analyze crowd wisdom and betting patterns
3. **Machine Learning:** Train models on market outcomes and prices
4. **Financial Research:** Study liquidity, volume, and price discovery
5. **Time Series Analysis:** Track event creation and market trends
6. **Network Analysis:** Study market relationships and competitiveness
7. **Sentiment Analysis:** Correlation between predictions and real outcomes

## Data Quality

- ✅ Complete pagination (all 2,192 pages)
- ✅ Zero data loss (nested arrays/objects preserved as JSON)
- ✅ 67 event fields captured (including dynamic fields from different event types)
- ✅ 106 market fields captured (complete market microstructure data)
- ✅ All timestamps in ISO 8601 format
- ✅ Numeric fields properly formatted

## Sample Insights

- **55% of all events** created in the last 30 days (explosive growth)
- **Fed decision event** leads with $14.96M in 24h volume
- **Strong correlation** between liquidity and trading volume (r > 0.8)
- **Binary markets dominate** with most events having 1-2 outcome markets
- **Crypto markets** represent over 50% of all events

## Data Format

- **File Format:** CSV (UTF-8 encoded)
- **Nested Structures:** JSON-encoded strings (parse with `json.loads()` in Python)
- **Missing Values:** Empty strings or null
- **Boolean Values:** "True"/"False" strings
- **Numeric Values:** Float format with full precision

## Usage Examples

### Python
```python
import pandas as pd
import json

# Load data
events = pd.read_csv('polymarket_events.csv')
markets = pd.read_csv('polymarket_markets.csv')

# Parse nested JSON
events['tags_parsed'] = events['tags'].apply(lambda x: json.loads(x) if pd.notna(x) else [])

# Analyze volume
print(f"Total Volume: ${events['volume'].sum()/1e9:.2f}B")
print(f"Top Event: {events.nlargest(1, 'volume24hr')['title'].values[0]}")
```

### R
```r
library(tidyverse)
library(jsonlite)

# Load data
events <- read_csv('polymarket_events.csv')
markets <- read_csv('polymarket_markets.csv')

# Parse JSON fields
events$tags_parsed <- lapply(events$tags, fromJSON)
```

## Related Links

- **GitHub Repository:** [Analysis Code & Visualizations](https://github.com/[your-username]/polymarket_com)
- **Polymarket Platform:** https://polymarket.com
- **API Documentation:** Gamma API public search endpoint

## Citation

If you use this dataset in your research, please cite:

```
Polymarket Prediction Markets Dataset (2025)
Collected from Polymarket Gamma API
Dataset available at: https://www.kaggle.com/datasets/ismetsemedov/polymarket
Collection Date: December 3, 2025
```

## License

This dataset is provided for research and educational purposes. Data sourced from Polymarket's public API. Please review Polymarket's Terms of Service for commercial use restrictions.

## Updates

This is a point-in-time snapshot from December 3, 2025. For real-time data, use the provided fetch script from the GitHub repository or query the Polymarket API directly.

## Tags

prediction-markets, polymarket, decentralized-finance, defi, blockchain, cryptocurrency, politics, sports-betting, market-data, financial-data, time-series, trading-volume, liquidity, economics, behavioral-economics
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
Event-level prediction market data with 87,680 events. Contains trading volume, liquidity, status, timestamps, categories, and market counts. All events from Polymarket platform (July 2022 - December 2025).
```

### polymarket_markets.csv
```
Market-level data with 201,590 individual prediction markets. Includes questions, outcomes, prices, order book data, trading activity, and resolution status. Links to parent events via event_id.
```

---

## Usability Rating

Aim for **10.0** by ensuring:
- ✅ Clear column names
- ✅ Comprehensive description
- ✅ Sample code provided
- ✅ Data quality documented
- ✅ Use cases explained
- ✅ Citation format included

---

## Collaborators (Optional)

You can add collaborators later if needed.

---

## Additional Metadata (Optional but Recommended)

### Update Frequency
```
Static Snapshot (December 3, 2025)
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
Automated collection using Python async requests (aiohttp) with complete pagination across 2,192 API pages
```

---

## Cover Image (Optional but Recommended)

**Suggestion:** Upload one of your generated charts as the cover image.

**Best options:**
1. `charts/01_top_events_volume.png` - Shows top events
2. `charts/03_volume_metrics.png` - Shows key metrics
3. `charts/07_liquidity_vs_volume.png` - Shows correlation scatter plot

This makes your dataset more visually appealing and increases discoverability.

---

## Tips for Maximum Visibility

1. **Use all relevant tags** - This helps with search
2. **Add cover image** - Datasets with images get more views
3. **Include sample code** - Makes dataset more accessible
4. **Link to GitHub** - Shows complete analysis
5. **Respond to comments** - Build community engagement
6. **Share on social media** - Cross-promote on Twitter/LinkedIn
7. **Write a kernel/notebook** - Create analysis notebook on Kaggle using your data

---

## Quick Checklist Before Upload

- [ ] CSV files are under 20GB (✓ You're at 600MB)
- [ ] Files are UTF-8 encoded (✓)
- [ ] No sensitive data included (✓)
- [ ] Description is clear and comprehensive (✓)
- [ ] Tags are relevant (✓)
- [ ] License is selected (Choose ODbL)
- [ ] Files have descriptions (✓)
- [ ] Cover image uploaded (Optional)
- [ ] Sample code provided (✓)

---

## Post-Upload Steps

1. **Create a Notebook** on Kaggle using your dataset
2. **Update GitHub README** with final Kaggle URL
3. **Share on social media** with #Polymarket #DataScience
4. **Monitor discussions** and answer questions
5. **Consider updating** the dataset monthly or quarterly

---

## Example Social Media Post

```
🚀 Just published a comprehensive Polymarket dataset on Kaggle!

📊 87,680 prediction market events
💰 $16B in trading volume
📈 201,590 individual markets
🗓️ 2.3 years of historical data

Perfect for ML, economics research, and market analysis!

🔗 https://www.kaggle.com/datasets/ismetsemedov/polymarket

#DataScience #PredictionMarkets #Polymarket #MachineLearning #DeFi
```
