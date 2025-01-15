from copy import deepcopy

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

m = int((n + δ)/2) + 1
l = int((α + β + γ + δ)/5) + 1

matrix = [[0, m-5, 0, (-1)**n],
          [(-1)**n*3, m-7, (-1)**n, 2],
          [2, 3, -l, 4],
          [m-2*l, -2, l-1, (-1)**n*3]]
print(f"m = {m}, l = {l}")
print(f"|A| = {Determinant(matrix)}")
print(matrix)   