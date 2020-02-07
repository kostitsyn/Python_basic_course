class Cell:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        sub = self.number - other.number
        if sub >= 0:
            return sub
        else:
            return 'Результат неверный (отрицательное число)'

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return int(self.number / other.number)

    def make_order(self, row):
        int_num = self.number // row
        rem_div = self.number % row
        result_list = ['*' * row for i in range(int_num)]
        result_list.append('*' * rem_div)
        print(f'Разбиваем количество клеток на {row} рядов:')
        print("\n".join(result_list))

creature_one = Cell(100)
creature_two = Cell(78)
print(f'Объединение двух клеток: {creature_one + creature_two}')
print(f'Разность двух клеток: {creature_one - creature_two}')
print(f'Произведение двух клеток: {creature_one * creature_two}')
try:
    print(f'Деление двух клеток: {creature_one / creature_two}')
except ZeroDivisionError:
    print('На ноль делить нельзя!')

creature_one.make_order(3)
