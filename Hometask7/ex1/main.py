'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

'''


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = '\n'.join('\t'.join(map(str, string)) for string in self.matrix)
        return result

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 33], [3, 4, 5]])
print(matrix_1)
print()

matrix_2 = Matrix([[15, 1, 2], [1, 10, 1]])
print(matrix_2)
print()

matrix_3 = Matrix([[1, 1, 2], [1, 1, 1]])
print(matrix_3)
print()

print(matrix_1 + matrix_2 + matrix_3)
print()
