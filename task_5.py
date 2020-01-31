import random

with open('text_5.txt', 'w') as f:
    low = int(input('Введите нижний предел диапазона: '))
    up = int(input('Введите верхний предел диапазона: '))
    num_list = []
    while len(num_list) < 10:
        num_list.append(random.randint(low, up))
    print(f"Набор рассмативаемых чисел:\n{' '.join(map(str, num_list))}")
    f.write('Набор рассматриваемых чисел:\n')
    for i, j in enumerate(num_list):
        f.write(f'{j} ')
        if i == (len(num_list) - 1):
            f.write('\n')
    sum_list = sum(num_list)
    print(f'Сумма чисел равна {sum_list}')
    f.write(f'Сумма чисел равна {sum_list}')
