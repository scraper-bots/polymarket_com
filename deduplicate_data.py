#!/usr/bin/env python3
"""
Deduplicate Polymarket CSV files
Removes duplicate records based on ID field
"""

import pandas as pd
from datetime import datetime

def deduplicate_csv(filename, id_column='id'):
    """Remove duplicates from CSV file"""
    print(f"\n{'=' * 80}")
    print(f"DEDUPLICATING: {filename}")
    print('=' * 80)

    # Load data with low_memory=False to avoid mixed type warnings
    print(f"Loading {filename}...")
    df = pd.read_csv(filename, low_memory=False)

    original_count = len(df)
    print(f"Original rows: {original_count:,}")
    print(f"Unique IDs: {df[id_column].nunique():,}")
    print(f"Duplicates: {original_count - df[id_column].nunique():,}")

    # Remove duplicates, keeping first occurrence
    print(f"\nRemoving duplicates (keeping first occurrence)...")
    df_clean = df.drop_duplicates(subset=[id_column], keep='first')

    final_count = len(df_clean)
    removed = original_count - final_count

    print(f"✓ Removed {removed:,} duplicate rows")
    print(f"✓ Final count: {final_count:,} unique rows")

    # Backup original
    backup_name = filename.replace('.csv', '_BACKUP.csv')
    print(f"\nBacking up original to {backup_name}...")
    df.to_csv(backup_name, index=False)
    print(f"✓ Backup saved")

    # Save deduplicated version
    print(f"\nSaving deduplicated data to {filename}...")
    df_clean.to_csv(filename, index=False)
    print(f"✓ Saved {final_count:,} rows")

    return original_count, final_count, removed


def main():
    """Main execution"""
    print("=" * 80)
    print("POLYMARKET DATA DEDUPLICATION")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Deduplicate events
    events_orig, events_final, events_removed = deduplicate_csv('polymarket_events.csv', 'id')

    # Deduplicate markets
    markets_orig, markets_final, markets_removed = deduplicate_csv('polymarket_markets.csv', 'id')

    # Summary
    print("\n" + "=" * 80)
    print("DEDUPLICATION SUMMARY")
    print("=" * 80)
    print(f"\nEVENTS:")
    print(f"  Before: {events_orig:,} rows")
    print(f"  After:  {events_final:,} rows")
    print(f"  Removed: {events_removed:,} duplicates ({events_removed/events_orig*100:.1f}%)")

    print(f"\nMARKETS:")
    print(f"  Before: {markets_orig:,} rows")
    print(f"  After:  {markets_final:,} rows")
    print(f"  Removed: {markets_removed:,} duplicates ({markets_removed/markets_orig*100:.1f}%)")

    print(f"\nTOTAL:")
    print(f"  Before: {events_orig + markets_orig:,} rows")
    print(f"  After:  {events_final + markets_final:,} rows")
    print(f"  Removed: {events_removed + markets_removed:,} duplicates")

    print("\n" + "=" * 80)
    print("DEDUPLICATION COMPLETE")
    print("=" * 80)
    print(f"✓ Original files backed up as *_BACKUP.csv")
    print(f"✓ Deduplicated files saved as polymarket_*.csv")
    print(f"✓ Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)


if __name__ == "__main__":
    main()
