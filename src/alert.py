# Zack Oakley
# 11/27/2025
# Filter events by magnitude threshold.

from typing import List, Dict
from .config import get_magnitude_threshold

# Given a list of normalized earthquake events, return only those those where 
#   magnitude >= EQ_MAGNITUDE_THRESHOLD from .env.
def filter_events_over_threshold(events: List[Dict]):
    threshold = get_magnitude_threshold()
    filtered = []
    for ev in events:
        mag = ev.get("magnitude")
        if mag is not None and mag >= threshold:
            filtered.append(ev)
    return filtered