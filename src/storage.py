import json

DATABASE = "data/missions.json"

def save_mission(name, points):

    mission = {
        "name": name,
        "waypoints": [
            {
                "lat": p.latitude,
                "lon": p.longitude
            }
            for p in points
        ]
    }

    with open(DATABASE, "w") as f:
        json.dump(mission, f, indent=4)
