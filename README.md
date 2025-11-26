# USGS-Earthquake-API-Warning


Example result from a call to endpoint https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson:



 "type": "FeatureCollection",
    "metadata": {
        "generated": 1764128060000,
        "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",
        "title": "USGS All Earthquakes, Past Hour",
        "status": 200,
        "api": "2.2.0",
        "count": 3
    },
    "features": [
        {
            "type": "Feature",
            "properties": {
                "mag": 1.3,
                "place": "10 km NNE of Healdsburg, CA",
                "time": 1764126755530,
                "updated": 1764127939572,
                "tz": null,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/nc75269371",
                "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc75269371.geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "automatic",
                "tsunami": 0,
                "sig": 26,
                "net": "nc",
                "code": "75269371",
                "ids": ",nc75269371,",
                "sources": ",nc,",
                "types": ",nearby-cities,origin,phase-data,scitech-link,",
                "nst": 21,
                "dmin": 0.0524,
                "rms": 0.03,
                "gap": 188,
                "magType": "md",
                "type": "earthquake",
                "title": "M 1.3 - 10 km NNE of Healdsburg, CA"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -122.820663452148,
                    38.6936683654785,
                    6.23000001907349
                ]
            },
            "id": "nc75269371"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 2.82,
                "place": "9 km SE of Sparks, Oklahoma",
                "time": 1764126222937,
                "updated": 1764127104608,
                "tz": null,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/ok2025xdio",
                "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ok2025xdio.geojson",
                "felt": 4,
                "cdi": 3.8,
                "mmi": null,
                "alert": null,
                "status": "automatic",
                "tsunami": 0,
                "sig": 124,
                "net": "ok",
                "code": "2025xdio",
                "ids": ",ok2025xdio,us7000rdux,",
                "sources": ",ok,us,",
                "types": ",dyfi,origin,phase-data,",
                "nst": 10,
                "dmin": 0.1040409207,
                "rms": 0.0978306609,
                "gap": 147.4173138,
                "magType": "ml",
                "type": "earthquake",
                "title": "M 2.8 - 9 km SE of Sparks, Oklahoma"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -96.74485779,
                    35.55410767,
                    4.656080246
                ]
            },
            "id": "ok2025xdio"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5,
                "place": "108 km NNE of Hihifo, Tonga",
                "time": 1764125952113,
                "updated": 1764127505040,
                "tz": null,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000rdv0",
                "detail": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us7000rdv0.geojson",
                "felt": null,
                "cdi": null,
                "mmi": null,
                "alert": null,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 385,
                "net": "us",
                "code": "7000rdv0",
                "ids": ",us7000rdv0,",
                "sources": ",us,",
                "types": ",origin,phase-data,",
                "nst": 40,
                "dmin": 2.022,
                "rms": 0.84,
                "gap": 101,
                "magType": "mb",
                "type": "earthquake",
                "title": "M 5.0 - 108 km NNE of Hihifo, Tonga"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -173.5422,
                    -15.0031,
                    10
                ]
            },
            "id": "us7000rdv0"
        }
    ],
    "bbox": [
        -173.5422,
        -15.0031,
        4.656080246,
        -96.74485779,
        38.693668365479,
        10
    ]
}