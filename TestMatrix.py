from copy import deepcopy

# Вычисление определителя матрицы
def Determinant(_matrix):
    order = len(_matrix)
    det = 0
    if order == 1: return _matrix[0][0]
    elif order == 2:
        return _matrix[0][0]*_matrix[1][1]-_matrix[0][1]*_matrix[1][0]
    elif order >= 3:
        for j in range(order):
            _matrix_ = deepcopy(_matrix)[1:]
            for item in _matrix_:
                item.pop(j)
            item = []
            det += (-1)**(j)*(_matrix[0][j])*(Determinant(_matrix_))
        return det
    else: return "Ошибка"

# Ввод матрицы
n = int(input("Введите порядок матрицы: "))
matrix = []
for i in range(n):
    stroka = [int(x) for x in input().split()]
    if len(stroka) != n:
        print("Неправильно введены данные!")
        break
    matrix.append(stroka)
# Вывод матрицы
print(f"|A| = {Determinant(matrix)}")