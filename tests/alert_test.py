from src.alert import filter_events_over_threshold
from src.config import get_magnitude_threshold

# Tests that only events with thresholds >= the set .env threshold are filtered out
def test_filter_events_over_threshold_reads_env_value():
    # Use the actual threshold from .env
    threshold = get_magnitude_threshold()

    events = [
        {"event_id": "a", "magnitude": threshold - 0.5},
        {"event_id": "b", "magnitude": threshold},
        {"event_id": "c", "magnitude": threshold + 0.8},
        {"event_id": "d", "magnitude": None},
    ]

    result = filter_events_over_threshold(events)
    ids = [e["event_id"] for e in result]

    # Only events with magnitude >= threshold should be returned
    assert ids == ["b", "c"]