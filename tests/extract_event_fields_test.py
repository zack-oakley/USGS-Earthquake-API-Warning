# Tests for extract_event_fields() in src/utils.py
# Verifies:
# - Correct extraction of all required fields for events
# - Proper handling of missing or null data without crashing
from src.utils import extract_event_fields

def test_extract_event_fields_full_event():
    # This is ONE feature from the USGS response (trimmed to what we need)
    raw_event = {
        "type": "Feature",
        "properties": {
            "mag": 0.96,
            "place": "5 km WNW of Calimesa, CA",
            "time": 1764211661350,
            "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ci41127871",
        },
        "geometry": {
            "type": "Point",
            "coordinates": [
                -117.107166666667,
                33.9998333333333,
                6.95,
            ],
        },
        "id": "ci41127871",
    }

    result = extract_event_fields(raw_event)

    # Basic field mapping
    assert result["event_id"] == "ci41127871"
    assert result["magnitude"] == 0.96
    assert result["place"] == "5 km WNW of Calimesa, CA"
    assert result["longitude"] == -117.107166666667
    assert result["latitude"] == 33.9998333333333
    assert result["depth_km"] == 6.95
    assert result["detail_url"] == "https://earthquake.usgs.gov/earthquakes/eventpage/ci41127871"

    # Time conversion: 1764211661350 ms → 2025-11-27T02:47:41Z
    assert result["time_utc"] == "2025-11-27T02:47:41Z"



def test_extract_event_fields_missing_fields():
    # Intentionally missing most fields to test "handle missing values"
    raw_event = {
        "type": "Feature",
        "properties": {
            # no mag, no place, no time, no url
        },
        "geometry": {
            # no coordinates
        },
        "id": None,
    }

    result = extract_event_fields(raw_event)

    # Everything should gracefully fall back to None, not crash
    assert result["event_id"] is None
    assert result["magnitude"] is None
    assert result["place"] is None
    assert result["latitude"] is None
    assert result["longitude"] is None
    assert result["depth_km"] is None
    assert result["detail_url"] is None
    assert result["time_utc"] is None