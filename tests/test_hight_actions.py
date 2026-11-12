import pet_data

def test_hight_actions():
    levels = {"feed": 60, "play": 40, "sleep": 80}
    assert pet_data.hight_actions(levels, 60) == ["sleep"]