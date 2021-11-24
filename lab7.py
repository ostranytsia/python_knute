from scipy.interpolate import lagrange
from numpy import *
import matplotlib.pyplot as plt
def jop(x):
    return 2*x**3-15*x+5
x = array([-4, -1, 1, 2],dtype =float)
y = array([-6, 3, -11, 6], dtype = float)
U = array([-3, -2, -0.5, 2.5])

def L(x, y, k):
    summa=0
    for g in range (len(y)):
        p1=1
        p2=1
        for i in range (len(y)):
            if i==g:
                p1 *= 1
                p2 *= 1
            else:
                p1*=(k-x[i])
                p2*=(x[g]-x[i])
        summa += y[g]*p1/p2
    return summa
xnew = linspace (min(x), max(x))
ynew = [L(x,y,i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.title('Lab7 | Ostranytsia Dmytro')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()
f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange polynomial')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()