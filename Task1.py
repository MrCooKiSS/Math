from copy import deepcopy


# Вычисление определителя матрицы методом треугольника
def Determinant1(_matrix):
    order = len(_matrix)
    det = 0
    if order == 3:
        for i in range(3):
            det += _matrix[0][i%3]*_matrix[1][(i+1)%3]*_matrix[2][(i+2)%3]
        for i in range(3):
            det -= _matrix[0][i%3]*_matrix[1][(i+2)%3]*_matrix[2][(i+1)%3]
        return det
    else:
        return "Ошибка"

# Вычисление определителя матрицы методом разложения по первой строке
def Determinant2(_matrix):
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
            det += (-1)**(j)*(_matrix[0][j])*(Determinant2(_matrix_))
        return det
    else:
        return "Ошибка"

# Ввод данных
n = int(input("Введите номер студента: "))
α = int(input("Введите α: "))
β = int(input("Введите β: "))
γ = int(input("Введите γ: "))
δ = int(input("Введите δ: "))
solutionsMethod = int(input("1) Метод треугольника, 2) Разложение по первой строке: "))

m = int((n + δ)/2) + 1
l = int((α + β + γ + δ)/5) + 1

matrix = [[(-1)**n*m, m-4*l, 2],
          [m-2*l, m-3*l, 5],
          [(-1)**n*2, -3, m-10]]
print(f"m = {m}, l = {l}")
# Выбор решения матрицы
if solutionsMethod == 1:
    print(f"|A| = {Determinant1(matrix)}")
elif solutionsMethod == 2:
    print(f"|A| = {Determinant2(matrix)}")
else:
    print("Ошибка!")
print(matrix)