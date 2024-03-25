import numpy as np

np.random.seed(0)

class MatrixOperatorsMixin:
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.data + other.data)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.data * other.data)
        else:
            return NotImplemented

    def __matmul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.data @ other.data)
        else:
            return NotImplemented

class GetterSetterMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


class StrMixin:
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.data)


class WriteToFileMixin:
    def write_to_file(self, path):
        with open(path, "w") as f:
            f.write(str(self))


class Matrix(GetterSetterMixin, StrMixin, WriteToFileMixin, MatrixOperatorsMixin):
    def __init__(self, data) -> None:
        self.data = data

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        if method == "__call__":
            scalars = []
            for arg in args:
                if isinstance(arg, self.__class__):
                    scalars.append(arg.data)
                else:
                    return NotImplemented
            return self.__class__(ufunc(*scalars, **kwargs))
        return NotImplemented


matrix1 = Matrix(data=np.random.randint(0, 10, (10, 10)))
matrix2 = Matrix(data=np.random.randint(0, 10, (10, 10)))

m_sum = matrix1 + matrix2
m_sum.write_to_file("artifacts/3.2/matrix_sum.txt")

m_mul = matrix1 * matrix2
m_mul.write_to_file("artifacts/3.2/matrix_mul.txt")

m_mmul = matrix1 @ matrix2
m_mmul.write_to_file("artifacts/3.2/matrix_mmul.txt")