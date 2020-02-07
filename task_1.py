from random import randint


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['  '.join([str(j) if j > 9 else str(j) + ' ' for j in i]) for i in self.matrix])

    def ghost_matr(self, other):
        if len(self.matrix) > len(other.matrix):
            dif_gen = len(self.matrix) - len(other.matrix)
            dif_elem = len(self.matrix[0]) - len(other.matrix[0])
            if dif_elem > 0:
                for z in range(len(other.matrix)):
                    for i in range(dif_elem):
                        other.matrix[z].append(0)
            else:
                for z in range(len(self.matrix)):
                    for i in range(abs(dif_elem)):
                        self.matrix[z].append(0)

            for i in range(dif_gen):
                l = [0 for i in range(len(self.matrix[0]))]
                other.matrix.append(l)
        elif len(self.matrix) < len(other.matrix):
            dif_gen = len(other.matrix) - len(self.matrix)
            dif_elem = len(other.matrix[0]) - len(self.matrix[0])
            if dif_elem > 0:
                for z in range(len(self.matrix)):
                    for i in range(dif_elem):
                        self.matrix[z].append(0)
            else:
                for z in range(len(other.matrix)):
                    for i in range(abs(dif_elem)):
                        other.matrix[z].append(0)

            for i in range(dif_gen):
                l = [0 for i in range(len(other.matrix[0]))]
                self.matrix.append(l)

    def __add__(self, other):
        Matrix.ghost_matr(self, other)
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in
                       range(len(self.matrix))])


matr_1 = Matrix([[randint(1, 20) for i in range(3)] for j in range(10)])
matr_2 = Matrix([[randint(1, 20) for i in range(2)] for j in range(11)])
print(f'Первая матрица\n{matr_1}')
print()
print(f'Вторая матрица\n{matr_2}')
print()
print(f'Сумма матриц\n{matr_1 + matr_2}')
