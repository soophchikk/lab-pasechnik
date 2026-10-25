start_age = 1
statrt_hunger = 50
start_mood = 50
start_energy = 50

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