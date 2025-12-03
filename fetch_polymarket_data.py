#!/usr/bin/env python3
"""
Polymarket Data Fetcher
Fetches ALL events from Polymarket API using async requests (active, closed, archived)
Saves events and markets data to CSV files without data loss
"""

import asyncio
import aiohttp
import csv
import json
from typing import List, Dict, Any
from datetime import datetime
import sys


BASE_URL = "https://gamma-api.polymarket.com/public-search"
PARAMS = {
    "q": "*",
    "limit_per_type": 20,
    "type": "events",
    # Removed events_status filter to fetch ALL events (active, closed, archived)
    "sort": "volume_24hr",
    "presets": ["EventsTitle", "Events"]
}


async def fetch_page(session: aiohttp.ClientSession, page: int) -> Dict[str, Any]:
    """Fetch a single page of events from the API"""
    params = PARAMS.copy()
    params["page"] = page

    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    async with session.get(BASE_URL, params=params, headers=headers) as response:
        response.raise_for_status()
        return await response.json()


async def fetch_all_pages(max_concurrent: int = 10) -> List[Dict[str, Any]]:
    """Fetch all pages concurrently with rate limiting"""
    all_events = []

    async with aiohttp.ClientSession() as session:
        # First, get the first page to determine total pages
        print("Fetching first page to determine total results...")
        first_page = await fetch_page(session, 1)

        total_results = first_page["pagination"]["totalResults"]
        events_per_page = len(first_page["events"])
        total_pages = (total_results + events_per_page - 1) // events_per_page

        print(f"Total results: {total_results}")
        print(f"Events per page: {events_per_page}")
        print(f"Total pages to fetch: {total_pages}")

        all_events.extend(first_page["events"])

        # Fetch remaining pages concurrently
        if total_pages > 1:
            print(f"\nFetching pages 2-{total_pages} with {max_concurrent} concurrent requests...")

            # Create batches to avoid overwhelming the server
            for batch_start in range(2, total_pages + 1, max_concurrent):
                batch_end = min(batch_start + max_concurrent, total_pages + 1)
                batch_pages = range(batch_start, batch_end)

                tasks = [fetch_page(session, page) for page in batch_pages]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                for page_num, result in zip(batch_pages, results):
                    if isinstance(result, Exception):
                        print(f"Error fetching page {page_num}: {result}", file=sys.stderr)
                        continue

                    all_events.extend(result["events"])
                    print(f"Fetched page {page_num}/{total_pages} ({len(all_events)} events so far)")

                # Small delay between batches
                if batch_end <= total_pages:
                    await asyncio.sleep(0.5)

    return all_events


def flatten_dict(data: Any, prefix: str = "") -> Any:
    """Convert nested structures to JSON strings for CSV compatibility"""
    if isinstance(data, dict):
        return json.dumps(data)
    elif isinstance(data, list):
        # Check if list contains primitives or complex objects
        if data and isinstance(data[0], (dict, list)):
            return json.dumps(data)
        else:
            return json.dumps(data)
    else:
        return data


def extract_events_data(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract event-level data (excluding markets)"""
    events_data = []

    for event in events:
        event_row = {}

        # Copy all fields except 'markets'
        for key, value in event.items():
            if key == "markets":
                # Store market count instead
                event_row["market_count"] = len(value) if value else 0
            else:
                event_row[key] = flatten_dict(value)

        events_data.append(event_row)

    return events_data


def extract_markets_data(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract all markets from events with event reference"""
    markets_data = []

    for event in events:
        event_id = event.get("id")
        event_slug = event.get("slug")
        event_title = event.get("title")

        markets = event.get("markets", [])
        for market in markets:
            market_row = {
                "event_id": event_id,
                "event_slug": event_slug,
                "event_title": event_title
            }

            # Add all market fields
            for key, value in market.items():
                market_row[key] = flatten_dict(value)

            markets_data.append(market_row)

    return markets_data


def save_to_csv(data: List[Dict[str, Any]], filename: str):
    """Save data to CSV file"""
    if not data:
        print(f"No data to save to {filename}")
        return

    # Get all unique keys from all dictionaries
    fieldnames = set()
    for row in data:
        fieldnames.update(row.keys())

    fieldnames = sorted(fieldnames)

    print(f"\nSaving {len(data)} rows to {filename}...")
    print(f"Columns: {len(fieldnames)}")

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"✓ Saved to {filename}")


async def main():
    """Main execution function"""
    print("=" * 80)
    print("POLYMARKET DATA FETCHER")
    print("=" * 80)
    print()

    start_time = datetime.now()

    # Fetch all events
    print("Step 1: Fetching all events from API...")
    events = await fetch_all_pages(max_concurrent=10)
    print(f"\n✓ Fetched {len(events)} events")

    # Extract and save events data
    print("\nStep 2: Extracting events data...")
    events_data = extract_events_data(events)
    save_to_csv(events_data, "polymarket_events.csv")

    # Extract and save markets data
    print("\nStep 3: Extracting markets data...")
    markets_data = extract_markets_data(events)
    save_to_csv(markets_data, "polymarket_markets.csv")

    # Summary
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total events fetched: {len(events)}")
    print(f"Total markets extracted: {len(markets_data)}")
    print(f"Time taken: {duration:.2f} seconds")
    print(f"\nFiles created:")
    print(f"  - polymarket_events.csv ({len(events_data)} rows)")
    print(f"  - polymarket_markets.csv ({len(markets_data)} rows)")
    print("=" * 80)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
