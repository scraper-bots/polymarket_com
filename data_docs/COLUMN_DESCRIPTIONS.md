# Column Descriptions for Kaggle Dataset

## polymarket_events.csv (67 columns)

### Identifiers
- **id** - Unique event identifier (integer)
- **slug** - URL-friendly event identifier (string)
- **ticker** - Short ticker symbol for the event (string)

### Event Information
- **title** - Full event title/question (string)
- **description** - Detailed event description with resolution criteria (text)
- **resolutionSource** - Source used to resolve the event outcome (string)
- **image** - URL to event cover image (URL)
- **icon** - URL to event icon (URL)

### Status Flags
- **active** - Whether event is currently active (boolean: True/False)
- **closed** - Whether event has closed (boolean: True/False)
- **archived** - Whether event is archived (boolean: True/False)
- **new** - Whether event is marked as new (boolean: True/False)
- **featured** - Whether event is featured on platform (boolean: True/False)
- **restricted** - Whether event has restrictions (boolean: True/False)

### Dates & Timestamps
- **startDate** - Event start date (ISO 8601 datetime)
- **endDate** - Event end date (ISO 8601 datetime)
- **createdAt** - Record creation timestamp (ISO 8601 datetime)
- **updatedAt** - Last update timestamp (ISO 8601 datetime)
- **creationDate** - Event creation date (ISO 8601 datetime)
- **closedTime** - Time when event closed (ISO 8601 datetime)

### Trading Metrics
- **volume** - Total all-time trading volume in USD (float)
- **volume24hr** - Trading volume in last 24 hours in USD (float)
- **volume1wk** - Trading volume in last 7 days in USD (float)
- **volume1mo** - Trading volume in last 30 days in USD (float)
- **volume1yr** - Trading volume in last 365 days in USD (float)
- **liquidity** - Total liquidity available in USD (float)
- **liquidityClob** - CLOB (Central Limit Order Book) liquidity in USD (float)
- **openInterest** - Open interest (unclosed positions) (float)

### Market Metrics
- **competitive** - Competitiveness score 0-1 (float)
- **commentCount** - Number of comments on event (integer)
- **market_count** - Number of markets within this event (integer)

### Order Book Features
- **enableOrderBook** - Whether order book is enabled (boolean: True/False)
- **negRisk** - Whether negative risk trading enabled (boolean: True/False)
- **negRiskMarketID** - Negative risk market identifier (string)
- **negRiskAugmented** - Enhanced negative risk features (boolean: True/False)

### Categories & Tags
- **tags** - JSON array of category tags with metadata (JSON string)
- **seriesSlug** - Series identifier if part of series (string)

### Sports-Specific Fields (when applicable)
- **homeTeamName** - Home team name for sports events (string)
- **awayTeamName** - Away team name for sports events (string)
- **score** - Current/final score for sports events (string)
- **gameId** - Game identifier for sports events (string)
- **eventDate** - Specific date of sports event (date)
- **eventWeek** - Week number for sports events (integer)
- **live** - Whether event is currently live (boolean: True/False)
- **elapsed** - Time elapsed in live event (string)
- **period** - Current period in sports event (string)

### Election-Specific Fields (when applicable)
- **electionType** - Type of election (string)
- **countryName** - Country for election events (string)
- **eventCreators** - JSON array of event creator info (JSON string)

### Technical Fields
- **cyom** - Custom market flag (boolean: True/False)
- **deploying** - Deployment status (boolean: True/False)
- **deployingTimestamp** - Deployment timestamp (ISO 8601 datetime)
- **pendingDeployment** - Pending deployment flag (boolean: True/False)
- **automaticallyActive** - Automatically activated flag (boolean: True/False)
- **showAllOutcomes** - Display all outcomes flag (boolean: True/False)
- **showMarketImages** - Display market images flag (boolean: True/False)
- **gmpChartMode** - Chart display mode (string)

### Display & Organization
- **featuredOrder** - Order in featured list (integer)
- **sortBy** - Sorting preference (string)
- **startTime** - Event start time (time)
- **finishedTimestamp** - Event finish timestamp (ISO 8601 datetime)
- **ended** - Whether event has ended (boolean: True/False)
- **tweetCount** - Number of related tweets (integer)
- **createdBy** - Creator user ID (string)
- **parentEventId** - Parent event ID if nested (string)
- **carouselMap** - Carousel display mapping (JSON string)

---

## polymarket_markets.csv (106 columns)

### Identifiers & References
- **id** - Unique market identifier (integer)
- **event_id** - Parent event ID (foreign key to events) (integer)
- **event_slug** - Parent event slug for reference (string)
- **event_title** - Parent event title for reference (string)
- **questionID** - Question identifier (string)
- **conditionId** - Blockchain condition ID (hex string)
- **slug** - URL-friendly market identifier (string)

### Market Question
- **question** - Market question/proposition (string)
- **description** - Detailed market description (text)

### Outcomes & Pricing
- **outcomes** - JSON array of possible outcomes (JSON string, e.g., ["Yes", "No"])
- **outcomePrices** - JSON array of current prices 0-1 (JSON string, e.g., ["0.45", "0.55"])
- **lastTradePrice** - Price of last executed trade (float)
- **oneDayPriceChange** - Price change in last 24h (float)
- **oneWeekPriceChange** - Price change in last 7 days (float)
- **oneMonthPriceChange** - Price change in last 30 days (float)

### Order Book
- **bestBid** - Best bid price (float)
- **bestAsk** - Best ask price (float)
- **spread** - Bid-ask spread (float)

### Trading Activity
- **volume** - Total all-time volume in USD (float)
- **volumeNum** - Volume as numeric (float)
- **volumeClob** - CLOB volume in USD (float)
- **volume24hr** - Volume last 24h in USD (float)
- **volume24hrClob** - CLOB volume last 24h in USD (float)
- **volume1wk** - Volume last 7 days in USD (float)
- **volume1wkClob** - CLOB volume last 7 days in USD (float)
- **volume1mo** - Volume last 30 days in USD (float)
- **volume1moClob** - CLOB volume last 30 days in USD (float)
- **volume1yr** - Volume last 365 days in USD (float)
- **volume1yrClob** - CLOB volume last 365 days in USD (float)

### Liquidity
- **liquidity** - Total liquidity in USD (float)
- **liquidityNum** - Liquidity as numeric (float)
- **liquidityClob** - CLOB liquidity in USD (float)

### Status Flags
- **active** - Whether market is active (boolean: True/False)
- **closed** - Whether market is closed (boolean: True/False)
- **archived** - Whether market is archived (boolean: True/False)
- **new** - Whether market is new (boolean: True/False)
- **featured** - Whether market is featured (boolean: True/False)
- **restricted** - Whether market is restricted (boolean: True/False)
- **approved** - Whether market is approved (boolean: True/False)

### Dates & Timestamps
- **startDate** - Market start date (ISO 8601 datetime)
- **startDateIso** - Start date ISO format (date)
- **endDate** - Market end date (ISO 8601 datetime)
- **endDateIso** - End date ISO format (date)
- **createdAt** - Creation timestamp (ISO 8601 datetime)
- **updatedAt** - Last update timestamp (ISO 8601 datetime)
- **acceptingOrdersTimestamp** - When orders accepted (ISO 8601 datetime)
- **hasReviewedDates** - Dates reviewed flag (boolean: True/False)

### Order Book Configuration
- **acceptingOrders** - Currently accepting orders (boolean: True/False)
- **enableOrderBook** - Order book enabled (boolean: True/False)
- **orderPriceMinTickSize** - Minimum price increment (float)
- **orderMinSize** - Minimum order size in USD (float)
- **clearBookOnStart** - Clear book on start flag (boolean: True/False)
- **rfqEnabled** - Request for quote enabled (boolean: True/False)

### Market Making
- **marketMakerAddress** - Market maker address (hex string)
- **rewardsMinSize** - Minimum size for rewards (float)
- **rewardsMaxSpread** - Maximum spread for rewards (float)

### Blockchain & Technical
- **clobTokenIds** - JSON array of CLOB token IDs (JSON string)
- **clobRewards** - JSON array of reward structures (JSON string)
- **negRisk** - Negative risk enabled (boolean: True/False)
- **negRiskMarketID** - Negative risk market ID (string)
- **negRiskRequestID** - Negative risk request ID (string)
- **negRiskOther** - Other negative risk params (string)
- **ready** - Market ready flag (boolean: True/False)
- **funded** - Market funded flag (boolean: True/False)

### Resolution
- **resolvedBy** - Address that resolved market (hex string)
- **umaReward** - UMA oracle reward amount (float)
- **umaBond** - UMA oracle bond amount (float)
- **customLiveness** - Custom liveness period seconds (integer)
- **umaResolutionStatuses** - UMA resolution status info (JSON string)
- **automaticallyResolved** - Auto-resolved flag (boolean: True/False)

### Display & Organization
- **groupItemTitle** - Title within group (string)
- **groupItemThreshold** - Threshold for grouping (float)
- **image** - Market image URL (URL)
- **icon** - Market icon URL (URL)
- **showGmpOutcome** - Show GMP outcome flag (boolean: True/False)
- **showGmpSeries** - Show GMP series flag (boolean: True/False)

### Submission & Creation
- **submitted_by** - Submitter address (hex string)
- **automaticallyActive** - Auto-activated flag (boolean: True/False)
- **cyom** - Custom market flag (boolean: True/False)
- **deploying** - Deployment status (boolean: True/False)
- **deployingTimestamp** - Deploy timestamp (ISO 8601 datetime)
- **pendingDeployment** - Pending deploy flag (boolean: True/False)
- **manualActivation** - Manual activation required (boolean: True/False)

### Additional Features
- **competitive** - Competitiveness score 0-1 (float)
- **feesEnabled** - Trading fees enabled (boolean: True/False)
- **holdingRewardsEnabled** - Holding rewards enabled (boolean: True/False)
- **pagerDutyNotificationEnabled** - PagerDuty alerts enabled (boolean: True/False)

---

## Data Types Legend

- **integer** - Whole number (e.g., 12345)
- **float** - Decimal number (e.g., 123.45)
- **string** - Text data (e.g., "Event Title")
- **text** - Long text content
- **boolean** - True/False values (stored as strings "True"/"False")
- **date** - Date only (YYYY-MM-DD)
- **time** - Time only (HH:MM:SS)
- **datetime** - Full timestamp (ISO 8601 format)
- **URL** - Web address
- **hex string** - Blockchain address (0x...)
- **JSON string** - JSON-encoded data (parse with json.loads() in Python)

## Missing Values

- Empty strings (`""`) indicate no value provided
- Some fields may be `null` or absent depending on event/market type
- Sports-specific fields only populated for sports events
- Election-specific fields only populated for election events
