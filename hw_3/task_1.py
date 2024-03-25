import numpy as np

np.random.seed(0)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Invalid matrix dimensions')
        product = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(product)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Invalid matrix dimensions')
        product = [[self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(product)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError('Invalid matrix dimensions')
        product = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)) for j in range(other.cols)]
                   for i in range(self.rows)]
        return Matrix(product)


def matrix_to_file(matrix, name):
    with open(name, 'w') as file:
        file.write(str(matrix))


matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

matrix_to_file(matrix1 + matrix2, 'artifacts/3.1/matrix_sum.txt')
matrix_to_file(matrix1 * matrix2, 'artifacts/3.1/matrix_mul.txt')
matrix_to_file(matrix1 @ matrix2, 'artifacts/3.1/matrix_mmul.txt')
