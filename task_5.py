from functools import reduce


def my_func(num_1, num_2):
    return num_1 * num_2


print(reduce(my_func, [i for i in range(100, 1001, 2)]))
