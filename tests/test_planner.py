from src.planner import Planner

def test_add_waypoint():

    planner = Planner()

    planner.add_waypoint(50, 30)

    assert len(planner.points) == 1
