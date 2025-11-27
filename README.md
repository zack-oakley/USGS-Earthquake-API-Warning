# USGS Earthquake Alert (Python + SQLite)

This project is an automated Python-based monitoring system that checks for recent earthquakes using the USGS Earthquake API. It retrieves earthquake data on a scheduled basis, stores events in a local SQLite database, evaluates whether any events exceed a configurable magnitude threshold, and sends an email alert when they do.

The goal is to simulate a real client project with a reliable end-to-end workflow that a non-technical user could set up and run.

# Features (Planned)
- Fetch recent earthquakes from the USGS **All Earthquakes, Past Hour** feed
- Parse and store events in a local **SQLite** database
- Prevent duplicate records using the USGS event ID as a unique key
- Compare magnitudes against a configurable **threshold** (e.g., 4.0)
- Send a **single consolidated email** if any events exceed the threshold
- Provide setup instructions for **Windows Task Scheduler** to run hourly

# Tech Stack
- **Language:** Python 3
- **Database:** SQLite (local file)
- **Dependencies:** (to be finalized in `requirements.txt`)
  - `requests` HTTP requests to USGS 
  - `python-dotenv` (environment variable loading)
  - `sqlite3` built-in SQLite database driver

# Project Structure
USGS-Earthquake-API-Warning/
│
├── src/
│ ├── app.py # Flask API endpoint to fetch parsed earthquakes
│ ├── utils.py # Field extraction and JSON transformation logic
│ └── db.py # (Upcoming) SQLite insert/retrieval logic
│
├── data/
│ └── earthquakes.db # SQLite database (git-ignored)
│
├── tests/
│ ├── test_utils.py # Unit tests for extract_event_fields
│ ├── test_db.py # Tests for DB logic 
│ └── test_api.py # Optional: tests for the /earthquakes endpoint
│
├── docs/
│ ├── requirements.md # Projects requirements & design notes
│ └── dev_time.md # Development notes & time tracking
│
├── .env # Environment config (not committed)
├── config.example.env # Example environment settings
├── .gitignore
├── requirements.txt
└── README.md