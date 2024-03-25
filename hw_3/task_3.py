import numpy as np

np.random.seed(0)

class MatrixHashMixin:
    def __hash__(self) -> int:
        # хэш-функция возвращающая уникальное значение на основе размера матрицы
        return hash((self.rows, self.cols))

class WriteToFileMixin:
    def write_to_file(self, path):
        with open(path, "w") as f:
            f.write(str(self))

class Matrix(MatrixHashMixin, WriteToFileMixin):
    def __init__(self, data):
        try:
            self.data = data
            self.rows = len(data)
            self.cols = len(data[0])
        except TypeError:
            raise ValueError()

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Invalid matrix dimensions')
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Invalid matrix dimensions')
        result = [
            [self.data[i][j] * other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError('Invalid matrix dimensions')
        result = [[
            sum(self.data[i][k] * other.data[k][j]
                for k in range(self.cols))
            for j in range(other.cols)]
            for i in range(self.rows)
            ]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


A = Matrix(np.random.randint(0, 10, (10, 10)))
B = Matrix(np.random.randint(0, 10, (10, 10)))
C = Matrix(np.random.randint(0, 10, (10, 10)))
D = B

collision = (hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D)
print("Коллизия: ", collision)

A.write_to_file('artifacts/3.3/A.txt')
B.write_to_file('artifacts/3.3/B.txt')
C.write_to_file('artifacts/3.3/C.txt')
D.write_to_file('artifacts/3.3/D.txt')

AB = A @ B
AB.write_to_file('artifacts/3.3/AB.txt')
CD = C @ D
CD.write_to_file('artifacts/3.3/CD.txt')

with open('artifacts/3.3/hash.txt', "w") as f:
    f.write('hash AB: ' + str(hash(AB)) + '\n')
    f.write('hash CD: ' + str(hash(CD)) + '\n')
