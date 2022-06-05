import math
import numpy as np
import cmath as cm #Для комплексных чисел


def printMatrix ( matrix ): 
   for i in range ( len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:2.2f}".format(matrix[i][j]), end = " ") 
      print('')
 
 
wide_arr = np.array([[9.0, 3.0, -3.0, -3.0],
              [3.0, 10.0, -4.0, -40.0],
              [-3.0, -4.0, 11.0, 50.0]])
n = len(wide_arr)
#Формирование матрицы t элементов
t_arr = np.zeros((wide_arr.shape), dtype = complex)
 
t_arr[0] = wide_arr[0]/cm.sqrt(wide_arr[0][0])
for i in range(1, n):
    t_arr[i][i] = cm.sqrt(wide_arr[i][i] - (t_arr[:,i]**2).sum()) 
    t_arr[i,i+1:] = (wide_arr[i,i+1:] - (t_arr[:i,i].reshape(-1,1)*t_arr[:i,i+1:]).sum(0))/t_arr[i][i]
 
#Находим решение
y = t_arr[:,n].reshape(-1,1)
t_arr = t_arr[:,:n]
x_arr = np.zeros((n,1), dtype = complex)
for i in range(1, n + 1):
    x_arr[-i, 0] = (y[-i] - (t_arr[-i, -i:] * x_arr[-i:, 0]).sum() )/ t_arr[-i, -i]
 
print('Матрица t,y элементов')
printMatrix(np.hstack((t_arr,y)))
print('Решение')
for i in range(1,n+1):
    print('x{} = {:2.3f}'.format( i, x_arr[i-1][0].real))