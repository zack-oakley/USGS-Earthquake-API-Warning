# Zack Oakley
# 11/27/2025
# Fetches recent USGS earthquakes, normalizes them, Inserts into SQLite,
#  avoiding duplicates, prints summary: "Fetched X events — inserted Y new"

import requests
from src.utils import extract_event_fields
from src.db import init_db, insert_earthquake

USGS_API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

def run_ingest():
    # Ensure DB and table exist
    init_db()

    # Fetch USGS feed
    response = requests.get(USGS_API_URL, timeout=5)
    response.raise_for_status()
    data = response.json()

    total_events = 0
    inserted_count = 0

    # Loop through all raw events
    for feature in data.get("features", []):
        total_events += 1

        # Normalize into our schema-friendly dict
        event_dict = extract_event_fields(feature)

        # Insert into DB if not already present
        inserted = insert_earthquake(event_dict)
        if inserted:
            inserted_count += 1

    print(f"Fetched {total_events} events — inserted {inserted_count} new")


if __name__ == "__main__":
    run_ingest()