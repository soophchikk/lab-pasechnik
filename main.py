print("===Тамагочи===")
name = input("Введите имя питомца:")
age = 1
hunger = 50
mood = 50
energy = 50

print("Питомец", name, "появился!")

while True:
    command = input("Введите команду (feed, play, sleep, status, rename, exit): ")
    if command == "feed":
        hunger = hunger - 20
        energy = energy + 5
        if hunger < 0:
            hunger = 0
        if energy > 100:
            energy = 100
        print(name, "покушал!")

    elif command == "play":
        mood = mood + 20
        energy = energy - 15
        hunger = hunger + 10
        if mood > 100:
            mood = 100
        if energy < 0:
            energy = 0
        if hunger > 100:
            hunger = 100
        print("Вы поиграли с", name)

    elif command == "sleep":
        energy = energy + 30
        hunger = hunger + 10
        if energy > 100:
            energy = 100
        if hunger > 100:
            hunger = 100
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
