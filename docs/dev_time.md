Development Time Log

Day 1 - 11/22/2025
Focus: Requirement gathering, planning, and task breakdown
Total Time: 3 Hours

Activities:
- Created requirements.md
- Created 18 work cards in a project Kanban
- Mock discussed and finalized client requirements

Notes:
- Planning took loner than expected

------------------------------------------------------

Day 2 - 11/25/2025
Focus: Desired API field identification
Total Time - 1.5 Hours

Activies
- Identify necessary fields from API call
- Determine SQLite Schema
- Create initial repo structure

Notes:
- N/A

------------------------------------------------------

Day 3 - 11/26/2025
Focus: Data extraction, API routing, testing infrastructure
Total Time - 4.5 Hours

Activites 
- Implemented the /earthquakes route in app.py to fetch live USGS data and transform it into event objects
- Created utils.py and implemented extract_event_fields() to:
    - extract nested JSON properties
    - handle missing .get() defaults
    - Convert epoch-millisecond timestamps into ISO-8601 UTC strings using    timezone-aware datetime
    - Map all fields to the future SQLite schema (event_id, magnitude, place, lat/lon, depth, etc.)
- Build a unit test extract_event_fields_test.py validating:
    - exxtraction of all required fields for a complete USGS event
    - Safe handling of missing or incomplete data
- Updated existing API tests api_test.py to match the new JSON output

Notes
- The system now correctly transforms raw USGS GeoJSON into a clean, database-ready format.
- Test suite confirms robust handling of real-world data, including missing fields.

------------------------------------------------------

Day 4 - 11/27/2025
Focus: Develop parsing and DB storage loop logic, and implement earthquake alert email utilities (threshold filtering, email body builder, SMTP send function)
Total Time - 4 Hours

Activities
- created get_events_over_threshold() in db.py to filter for evetns over a threshold
    in earthquakes.db
- created utils.py to extract required fields from a USGS earthquake event
- created a unit test for the function extract_event_fileds_test in utils.py
- populated .env with correct values
- created alert.py that takes a list of earthquake events as a list of dictionaries.
    returns the events that have a magnitude greater than what is defined in .env
- created a unity test alert_test.py to test alert.py

Notes
- Still need to integrate alert logic into ingest.py so that after inserting new events,
    the script automatically filters high-magnitude events and sends an email alert
- Email utility module is fully implemented and ready for integration

------------------------------------------------------

Day 5 - 
Focus:
Total Time - 

Activities

Notes

------------------------------------------------------

Day 6 - 
Focus:
Total Time - 

Activities

Notes

------------------------------------------------------

Day 7 - 
Focus:
Total Time - 

Activities

Notes