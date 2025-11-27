# Zack Oakley
# 11/26/2025
# Flask API to retrieve earthquake data from USGS
from flask import Flask, request, jsonify
import requests
from .utils import extract_event_fields


app = Flask(__name__)

USGS_API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"


# Route to get JSON data of earthquakes within the past hour
@app.get("/earthquakes")
def get_earthquakes():
    try:
        response = requests.get(USGS_API_URL)
        data = response.json()

        # Use util function to append all json objects into an events list
        events = []
        for feature in data.get("features", []):
            events.append(extract_event_fields(feature))

        return jsonify(events), 200
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch earthquake data"}), 502


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8010, debug=True)