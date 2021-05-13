'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

'''

from copy import deepcopy

class Matrix():

    def __init__(self, matrix_num):
        self.matrix = deepcopy(matrix_num)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __str__(self):
        return '\n'.join(' '.join(map(str, line)) for line in self.matrix)

    def __add__(self, other):
        result = []
        sumline = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sumline.append(other[i][j] + self.matrix[i][j])
                if len(sumline) == len(self.matrix[i]):
                    result.append(sumline)
                    sumline = []
        return Matrix(result)

your_matrix = Matrix([[31, 33], [37, 43], [51, 86]])
my_matrix = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
add_matrix = your_matrix + my_matrix
print(add_matrix)
print(type(add_matrix))
