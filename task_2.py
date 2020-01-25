try:
    num_list = list(map(int, input('Введите список целых чисел через пробел: ').split()))
except ValueError:
    print('Вводите только целые числа и только через один пробел!')

print([j for i, j in enumerate(num_list) if num_list[i - 1] < num_list[i] and i > 0])
