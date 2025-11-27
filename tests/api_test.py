from src.app import app


# Test USGS API
def test_earthquakes_route():
    client = app.test_client()
    response = client.get("/earthquakes")
    data = response.get_json()
    
    assert response.status_code == 200

    if data:  # only check contents if the list isn't empty
        event = data[0]
        assert "event_id" in event
        assert "time_utc" in event
        assert "magnitude" in event
        assert "place" in event
        assert "latitude" in event
        assert "longitude" in event
        assert "depth_km" in event
        assert "detail_url" in event
    