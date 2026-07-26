import json

def export_json(name, points):

    filename = f"data/exported/{name}.json"

    data = {
        "mission": name,
        "waypoints": [
            {
                "latitude": p.latitude,
                "longitude": p.longitude
            }
            for p in points
        ]
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print("Mission exported.")
