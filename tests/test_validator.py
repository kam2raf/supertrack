from src.validator import valid_latitude, valid_longitude

def test_latitude():
    assert valid_latitude(45)

def test_longitude():
    assert valid_longitude(120)
