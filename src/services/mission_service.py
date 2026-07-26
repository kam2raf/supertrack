from validator import valid_latitude, valid_longitude

def add_point(points, lat, lon):

    if not valid_latitude(lat):
        raise ValueError("Invalid latitude")

    if not valid_longitude(lon):
        raise ValueError("Invalid longitude")

    points.append((lat, lon))
