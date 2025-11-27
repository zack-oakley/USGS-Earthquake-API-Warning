# Zack Oakley
# 11/26/2025
# Extract required fields from a USGS earthquake event
from datetime import datetime, timezone

def extract_event_fields(event: dict):
    props = event.get("properties", {})
    geom = event.get("geometry", {})

    # Coordinates safely extracted
    coords = geom.get("coordinates", [None, None, None])
    longitude = coords[0]
    latitude = coords[1]
    depth_km = coords[2]

    # Convert epoch milliseconds → ISO8601 UTC string for DB
    timestamp = props.get("time")
    if isinstance(timestamp, int):
        # USGS timestamps are in milliseconds
        dt = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc)
        time_utc = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        time_utc = None

    return {
        "event_id": event.get("id"),
        "time_utc": time_utc,
        "magnitude": props.get("mag"),
        "place": props.get("place"),
        "latitude": latitude,
        "longitude": longitude,
        "depth_km": depth_km,
        "detail_url": props.get("url"),
    }
