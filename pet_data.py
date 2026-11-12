start_age = 1
start_hunger = 50
start_mood = 50
start_energy = 50

actions =  ["feed", "play", "sleep"]

levels = {"feed": 60, "play": 55, "sleep": 80}

used_actions = set()

def clamp(value, low=0, high=100):
    return max(low, min(value, high))

def feed(hunger):
    hunger = clamp(hunger - 20, 0, 100)
    return hunger

def play(mood):
    mood = clamp(mood + 20, 0, 100)
    return mood

def sleep(energy):
    energy = clamp(energy + 30, 0, 100)
    return energy

def show_help():
    print("===Доступные команды===")
    print("feed - покормить питомца")
    print("play - поиграть с питомцем")
    print("sleep - уложить питомца спать")
    print("status - показать статус питомца")
    print("rename - переименовать питомца")
    print("exit - выйти из игры")

def hight_actions(levels, threshold):
    return [a for a, l in levels.items() if l > threshold]

def add_actions(used, a):
    used.add(a)

def average(levels):
    if len(levels) == 0:
        return 0
    return sum(levels.values()) / len(levels)

def actions_upper(actions):
    return [a.upper() for a in actions]