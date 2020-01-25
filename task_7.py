def fact(n):
    num = 1
    for i in range(1, n + 1):
        if i > 20:
            break
        num = i * num
        yield num


for i, j in enumerate(fact(int(input('Введите число для получения его факториала: '))), 1):
    print(f'{i}!={j}')
