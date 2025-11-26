1) Overview:
This project is an automated Python-based monitoring system that checks
for recent earthquakes using the USGS Earthquake API. The script retrieves
updated earthquake data on a scheduled basis (hourly), stores the events in a
local SQLite database, evaluates whether any earthquakes exceed a configurable
magnitude threshold, and sends an automated email alert when necessary.

The goal is to create a reliable end-to-end workflow suitable for a non-technical user, replicating the scope and structure of a real client project.

2) Functional Requirements:
Data Retrieval:
Fetch JSON data from the USGS endpoint: https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson, Handle HTTP/network errors without crashing, Log or print clear error messages if the request fails. 

Data Parsing:
Extract at a minimum: Event Id, Magnitude, Time, Place/Description, Lat, Long, USGS detail URL (Validate teh the required fields exist)

Data Storage:
Use SQLite as local database engine. Create a table (earthquakes maybe?) with appropriate columns and types. Insert new earthquake events into the database. Prevent duplicate entries using the USGS event ID as a unique key

Threshold Evaluation:
Compare event's magnitude to a configurable threshold (default: 4.0). Identify all events from the current run that exceed this threshold

Email Alerts:
If zero events meet the threshold then no alert is sent. If one or more events meet the threshold: Send one consolidated email summarizing all matching events. Subject format: Earthquake Alert - {N} event(s) above magnitue {Threshold}. Body includes Magnitude, Time, Place, USGS detail URL

Configuration:
Store configurable values in a .env file: Threshold, EMAIL_USER, EMAIL_PASS, EMAIL_TO, SERVER, PORT

Execution Flow:
The script performs a single full cycle and exits. Scheduling of recurring runds will be handled by Windows Task Scheduler and documented in the README

3) Non-Functional Requirements:
Script should finish executing in under 5 seconds. Documentation must be understandable by a non-technical user. Email must be sent once per one, even if multiple events qualify

4) Data Model
CREATE TABLE IF NOT EXISTS earthquakes (
    event_id    TEXT PRIMARY KEY,
    time_utc    TEXT,        -- ISO 8601 string, e.g. "2025-11-25T08:15:00Z"
    magnitude   REAL,
    place       TEXT,
    latitude    REAL,
    longitude   REAL,
    depth_km    REAL,
    detail_url  TEXT
);

JSON -> DB Mapping:
features[i].id → event_id
features[i].properties.mag → magnitude
features[i].properties.place → place
features[i].properties.time → time
features[i].properties.url → detail_url
features[i].geometry.coordinates[1] → latitude
features[i].geometry.coordinates[0] → longitude
features[i].geometry.coordinates[2] → depth_km


5) Deliverables:
The final project must include: app.py (main script containing the workflow), requirements.txt, README.md with setup instrcutions, .env configuration instructions. How to manually run and how to schedule with Windows Task Scheduler. 

6) Acceptance Criteria:
Data Flow:
Running python app.py fetches JSON, parses it, stores events, and performs threshold checks. API do not crash the script

Database:
Database file is created on first run. New earthquake entries appear in the table. No duplicates.

Email:
If no events exceed threshold then no email send. If events exceed threshold: email is delivered successfully. Email contains all required event details.

Documentation:
README allows a non-technical user to set up: Python environment, .env, dependencies, Task Scheduler automation

7) Assumptions
User can follow basic setup/install instructions.