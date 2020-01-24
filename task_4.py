def exp_num_1(x, y):
    """Возведение в степень.

       Позиционные параметры:
       x -- основание степени
       y -- степень
       Первый способ - через оператор *


       """
    return x ** y


def exp_num_2(x, y):
    """Второй способ"""
    rezult = 1
    while abs(y):
        rezult = rezult / (1 / x)
        y += 1
    rezult = 1 / rezult
    return rezult


while True:
    try:
        x = float(input("Введите действительное положительное число 'x': "))
        y = int(input("Введите целое отрицательное число 'y': "))
    except ValueError:
        print("'x' должен быть действительным положительным числом, а 'y' должен быть целым отрицательным числом")
        continue
    if x > 0 and y < 0:
        break
    else:
        print("'x' должен быть действительным положительным числом, а 'y' должен быть целым отрицательным числом")
print(f'{x} в степени {y} равно {round(exp_num_1(x, y), 2)}')
print(f'{x} в степени {y} равно {round(exp_num_2(x, y), 2)}')
