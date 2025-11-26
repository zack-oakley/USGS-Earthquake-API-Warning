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
  - `requests` (HTTP requests)
  - `python-dotenv` (environment variable loading)
  - `sqlite3` (standard lib)

# Project Structure
USGS-Earthquake-API-Warning/
│
├── src/
│   └── app.py              # Main application entry point (WIP)
│
├── data/                   # SQLite DB + logs (ignored by git)
│
├── tests/                  # Future unit tests
│
├── docs/
│   ├── requirements.md     # Detailed project requirements/spec
│   └── dev_time.md         # Time tracking & notes
│
├── .env                    # Local environment config (not committed)
├── config.example.env      # Example config for users
├── .gitignore
├── requirements.txt        # Python dependencies
└── README.md