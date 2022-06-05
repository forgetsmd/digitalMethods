import math
import numpy as np

myA=[
 [-34.0, -26.0, 0.0, 0.0, 0.0],
 [64.0, -124.0, -56.0, 0.0, 0.0],
 [0.0, 94.0, -274.0, -86.0, 0.0],
 [0.0, 0.0, 124.0, -484.0, -116.0],
 [0.0, 0.0, 0.0, 154.0, -754.0]
]
n = len(myA)

myB = [
 34.0,
 38.0,
 42.0,
 46.0,
 50.0]

#прогоночные коэф.
P = [0.0 for k in range(0, n+1, 1)]
Q = [0.0 for k in range(0, n+1, 1)]
X = [0.0 for k in range(0, n, 1)]


def Progon(myA, myB):
	#прямой ход ( вычисляем по формулам прогоночные коэф. начиная с Q1 и P1 )
	for i in range(n):
		#для первой и последней итерации формулы изменяются из-за отсутствия а(1) и с(n)
		if i == 0:
			P[i+1] = (-myA[i][i+1])/(myA[i][i])
			Q[i+1] = (myB[i])/(myA[i][i])
		elif i == n-1:
			Q[i+1] = (myB[i] - myA[i][i-1]*Q[i])/(myA[i][i] + myA[i][i-1]*P[i])
		else:
			P[i+1]=(-myA[i][i+1])/(myA[i][i] + myA[i][i-1]*P[i])
			Q[i+1] = (myB[i] - myA[i][i-1]*Q[i])/(myA[i][i] + myA[i][i-1]*P[i])
	#обратный ход ( вычисляем Х, начиная с Х(n) )
	for r in range(n-1, -1, -1):
		if r == n-1:
			X[r] = Q[r+1]
		else:
			X[r] = Q[r+1] + P[r+1]*X[r+1]		
	return X
print(Progon(myA,myB))

