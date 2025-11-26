from src.app import app


# Test USGS API
def test_earthquakes_route():
    client = app.test_client()
    response = client.get("/earthquakes")
    data = response.get_json()
    
    assert response.status_code == 200
    assert "features" in data
    