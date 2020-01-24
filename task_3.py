def my_func(number_1, number_2, number_3):
    """Возвращает сумму наибольших двух чисел"""
    return sum([number_1, number_2, number_3]) - min([number_1, number_2, number_3])


while True:
    try:
        my_list = input('Введите 3 числа: ').split()
        for i in my_list:
            elem = my_list.pop(0)
            my_list.append(int(elem))
        num_1, num_2, num_3 = my_list
        print(f'Сумма наибольших двух чисел равна {my_func(num_1, num_2, num_3)}')
        break
    except ValueError:
        print('Нужно ввести числа!')
