while True:
    print("Выберите один из трех вариантов:\n1. Нарисуйте квадрат\n2. Нарисуйте башню вверх ногами\n3. Выход")
    choice = input("Введите номер выбранного варианта: ")

    if choice == "1":
        while True:
            size_input = input("Введите размер квадрата: ")
            try:
                size = int(size_input)
                if size >= 0:
                    break
                else:
                    print("Размер квадрата должен быть числом.")
            except ValueError:
                print("Размер квадрата должен быть целым числом.")

        for i in range(size):
            if i == 0 or i != size:
                print(" " + "█" * (size * 2) + " ")

        print()

    elif choice == "2":
        height = int(input("Введите высоту башни: "))
        size = height * 2 - 1
        for i in range(height):
            s = " " * (i) + "█" * size + " " * (i)
            print(s)
            size -= 2

    elif choice == "3":
        break

    else:
        print("Неверный выбор, повторите попытку.")