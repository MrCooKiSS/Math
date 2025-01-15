from copy import deepcopy

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

matrix = [[3, -2, 4, 21],
          [3, 4, -2, 9],
          [2, -1, -1, 10]]

for i in range(len(matrix[0])):
    matrix_ = KramerMethod(matrix, i)
    print(f"{i} = {Determinant(matrix_)}")