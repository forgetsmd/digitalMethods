import math
import numpy as np

myA=[
 [6.0, -1.0, 0.0, 0.0],
 [-3.0, 4.0, -6.0, 0.0],
 [0.0, 2.0, 1.0, -7.0],
 [0.0, 0.0, -3.0, 1.0]
]

myB = [
 5.0,
 -5.0,
 -4.0,
 -2.0]

#перемена местами двух строк системы
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]

#деление строки системы на число
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider

#сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight

def Gauss(A, B):
    column = 0
    while (column < len(B)):
        current_row = 0
		#ищем наибольший коэф. в столбце:
        for r in range(column, len(A)):
            if abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row != column:
            SwapRows(A, B, current_row, column)
		#делим выбранную строку на диагональный элемент, чтобы привести его к 1:
        DivideRow(A, B, column, A[column][column])
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        column += 1
    X = [0 for b in B]
	#вычисляем X
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    return X
print(Gauss(myA, myB))
#находим определитель по гауссу(перемножаем эл-ты главюдиагонали)
detA = 1.0
for i in range(len(myA)):
	detA *= myA[i][i]
print(detA)