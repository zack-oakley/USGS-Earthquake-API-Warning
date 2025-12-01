# Zack Oakley
# 11/27/2025
# Fetches recent USGS earthquakes, normalizes them, Inserts into SQLite,
#  avoiding duplicates, prints summary: "Fetched X events — inserted Y new"

import requests
from src.utils import extract_event_fields
from src.db import init_db, insert_earthquake
from src.config import get_magnitude_threshold
from src.alert import filter_events_over_threshold
from src.emails_utils import build_email_body, send_email

USGS_API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

# Fetches raw earthquake data from the USGS API. Returns the 'features' list from the JSON response
def retrieve_events():
    # Fetch USGS feed
    response = requests.get(USGS_API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("features", [])


def main():
    # Ensure DB and tables exist
    init_db()

    # retrieve raw usgs events
    raw_events = retrieve_events()

    # normalize and insert into DB
    normalized_events = []
    for feature in raw_events:
        event = extract_event_fields(feature)
        normalized_events.append(event)
        insert_earthquake(event)

    # Filter over threshold and decide whether to send email
    threshold = get_magnitude_threshold()
    over_threshold = filter_events_over_threshold(normalized_events)
    event_count = len(over_threshold)
    if event_count == 0:
        print(f"No events at or exceed  {threshold}.")
        return
    
    # Build and send email
    subject = f"[USGS Alert] {event_count} earthquakes ≥ M {threshold}"
    body = build_email_body(over_threshold)
    try:
        send_email(subject, body)
        print(f"Alert email sent for {event_count} earthquakes ≥ magnitude {threshold}.")
    except Exception as exc:
        # Don't crash the whole ingest job on email failure
        print(f"Failed to send alert email: {exc}")


if __name__ == "__main__":
    main()