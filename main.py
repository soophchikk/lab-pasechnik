from pet_data import start_age, statrt_hunger, start_mood, start_energy, clamp

print("===Тамагочи===")
name = input("Введите имя питомца:")
age = start_age
hunger =  statrt_hunger
mood = start_mood
energy = start_energy

print("Питомец", name, "появился!")

while True:
    command = input("Введите команду (feed, play, sleep, status, rename, exit): ")
    if command == "feed":
        hunger = clamp(hunger - 20, 0, 100)
        energy = clamp(energy + 5, 0, 100)
        print(name, "покушал!")

    elif command == "play":
        mood = clamp(mood + 20, 0, 100)
        energy = clamp(energy - 15, 0, 100)
        hunger = clamp(hunger + 10, 0, 100)
        print("Вы поиграли с", name)

    elif command == "sleep":
        energy = clamp(energy + 30, 0, 100)
        hunger = clamp(hunger + 10, 0, 100)
        print(name, "поспал!")

    elif command == "status":
        print("Имя:", name)
        print("Возраст:", age)
        print("Голод:", hunger)
        print("Настроение:", mood)
        print("Энергия:", energy)

        if mood <= 10 and energy <= 10 and hunger >= 80:
            print("Питомец плохо себя чувствует!")
        else:
            if hunger >= 80:
                print("Питомец очень голоден!")
            if mood <= 10:
                print("Питомец грустит!")
            if energy <= 20:
                print("Питомец сильно устал!")
            if hunger < 70 and mood > 10 and energy > 10:
                print("Питомец хорошо себя чувствует!")

    elif command == "rename":
        new_name = input("Введите новое имя: ")

        if new_name != "":
            name = new_name
            print("Теперь питомца зовут", name)
        else:
            print("Имя не может быть пустым!")

    elif command == "exit":
        print("Игра завершена!")
        break

    else:
        print("Неизвестная команда!")
