with open('text_3.txt', 'r') as f:
    sum = 0
    print('Сотрудники с окладом менее 20000:')
    for num, line in enumerate(f, 1):
        a = line.split()
        if float(a[1]) < 20000:
            print(a[0])
        sum += float(a[1])
    print(f'Средняя зарплата сотрудников составляет {round(sum / num, 2)}')
