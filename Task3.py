from copy import deepcopy

# Создание матрицы по методу Крамера
def KramerMethod(_matrix, _x):
    lenght = len(_matrix[0])
    matrix = deepcopy(_matrix)
    if _x != 0:
        for i in range(len(matrix)):
            matrix[i][_x-1] = matrix[i].pop(lenght-1)
    else:
        for i in matrix:
            i.pop(lenght-1)
    return matrix

# Вычисление определителя матрицы методом разложения по первой строке
def Determinant(_matrix):
    order = len(_matrix)
    det = 0
    if order == 1:
        return _matrix[0][0]
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
    else:
        return "Ошибка"

# Ввод данных
n = int(input("Введите номер студента: "))
α = int(input("Введите α: "))
β = int(input("Введите β: "))
γ = int(input("Введите γ: "))
δ = int(input("Введите δ: "))

# Рассчет переменных и матрицы
m = int((n + δ)/2) + 1
l = int((α + β + γ + δ)/5) + 1

matrix = [[(-1)**n*(m+1), -(m+3), (-1)**n*2],
          [(-1)**(n+1)*(l+3), l+1, (-1)**(n+1)*2*(l+m+3)]]
DetMainMatrix = Determinant(KramerMethod(matrix, 0))

# Вывод
print(f"m = {m}, l = {l}")
for i in range(1, len(matrix[0])):
    print(f"x{i} = {Determinant(KramerMethod(matrix, i))/DetMainMatrix}")