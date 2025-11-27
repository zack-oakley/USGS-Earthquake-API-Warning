# Zack Oakley
# 11/26/2025
# Initializes earthquakes.db, handles returning a single earthquake, and inserting 
#   an earthquake
import sqlite3
import os

DB_PATH = "data/earthquakes.db"

# Creates the the earthquakes.db file (if it doesnt exist) and initializes the earthquakes
#   table with correct schema
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Create table if it does not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS earthquakes (
            event_id    TEXT PRIMARY KEY,
            time_utc    TEXT,
            magnitude   REAL,
            place       TEXT,
            latitude    REAL,
            longitude   REAL,
            depth_km    REAL,
            detail_url  TEXT
        );
    """)

    # save changes
    conn.commit()
    conn.close()


# Returns the earthquake row for the given event_id, or None if not found
def get_earthquake(event_id: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT event_id, time_utc, magnitude, place,
               latitude, longitude, depth_km, detail_url
        FROM earthquakes
        WHERE event_id = ?;
    """, (event_id,))

    row = cur.fetchone()
    conn.close()
    return row

# Inserts an earthquake record if event_id iss not already present. Retruns
#   True if a new row was inserted
#   False if event_id already existed
def insert_earthquak(event: dict):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

     # 1) Check if this event_id already exists
    cur.execute("SELECT 1 FROM earthquakes WHERE event_id = ?;", (event["event_id"],))
    exists = cur.fetchone() is not None

    if exists:
        conn.close()
        return False  # No insert, already in DB

    # 2) Insert new row
    cur.execute("""
        INSERT INTO earthquakes (
            event_id, time_utc, magnitude, place,
            latitude, longitude, depth_km, detail_url
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        event["event_id"],
        event["time_utc"],
        event["magnitude"],
        event["place"],
        event["latitude"],
        event["longitude"],
        event["depth_km"],
        event["detail_url"],
    ))

    conn.commit()
    conn.close()


    return True

if __name__ == "__main__":
    init_db()