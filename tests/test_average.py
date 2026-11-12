import pet_data

def test_average():
    levels = {"feed": 60, "play": 40}
    assert pet_data.average(levels) == 50