from math import cos
 
def func(x) :
    return cos(2 * x) + (0.165* x* x - 1) * x 
 
a = -3
b = 3
c = (a + b) / 2
eps = 1e-5
while abs(func(c)) > eps :
    res = func(c)
    if res < 0 :
        a = c 
    else :
        b = c 
    c = (a + b) / 2
print('%.6f' % c)