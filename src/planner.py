from models import Waypoint
from storage import save_mission
from exporter import export_json

class Planner:

    def __init__(self):
        self.points = []

    def add_waypoint(self, lat, lon):
        self.points.append(Waypoint(lat, lon))

    def save(self, name):
        save_mission(name, self.points)

    def export(self, name):
        export_json(name, self.points)
