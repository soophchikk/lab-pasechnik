import pet_data

def test_add_actions():
    used = set()
    pet_data.add_actions(used, "feed")
    assert "feed" in used  