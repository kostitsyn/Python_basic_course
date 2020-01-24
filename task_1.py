while True:
    try:
        one = int(input('Введите делимое: '))
        two = int(input('Введите делитель: '))
    except ValueError:
        print('Нужно ввести число!')
        continue

    try:
        print((lambda num_1, num_2: num_1 / num_2)(one, two))
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
        break
