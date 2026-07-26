from dataclasses import dataclass

@dataclass
class Waypoint:

    latitude: float
    longitude: float


@dataclass
class Mission:

    name: str
    waypoints: list
