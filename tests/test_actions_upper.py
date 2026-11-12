import pet_data

def test_actions_upper():
    actions = ["feed", "play", "sleep"]

    assert pet_data.actions_upper(actions) == ["FEED", "PLAY", "SLEEP"]