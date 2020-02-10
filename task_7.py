class Complex_num:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        # self.sum = self.num + other.num
        return f'Сумма {self.num + other.num}'


    def __mul__(self, other):
        return f'Произведение {self.num * other.num}'




num_1 = Complex_num(complex(2, 3))
num_2 = Complex_num(complex(4, 6))
print(num_1 + num_2)
print(num_1 * num_2)

