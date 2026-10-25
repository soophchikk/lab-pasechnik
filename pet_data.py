start_age = 1
statrt_hunger = 50
start_mood = 50
start_energy = 50

def clamp(value, low=0, high=100):
    return max(low, min(value, high))