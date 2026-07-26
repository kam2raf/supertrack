from planner import Planner

planner = Planner()

planner.add_waypoint(50.4501, 30.5234)
planner.add_waypoint(50.4518, 30.5251)
planner.add_waypoint(50.4534, 30.5280)

planner.save("Forest Patrol")
planner.export("Forest Patrol")
