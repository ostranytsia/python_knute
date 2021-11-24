import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
def fac1(i1, qq1):
    j1=1
    dq1=1
    while j1<=i1:
        dq1*=qq1 - j1
        j1+=1
    return dq1

def fac2(i2, qq2):
    j2=1
    dq2=1
    while j2<=i2:
        dq2*=qq2 + j2
        j2+=1
    return dq2

mas_x=[1.340,1.345,1.350,1.355,1.360,1.365,1.370,1.375,1.380,1.385,1.390]
mas_y=[4.2556 ,4.3532, 4.4552, 4.5618, 4.6734, 4.7903, 4.9130, 5.0419, 5.1774, 5.3201, 5.4706]
h = mas_x[1] - mas_x[0]
x=0.1
xo=0
xn=1.390
q=(x-xo)/h
k=0
def y(mas_y,j):
    mas=[]
    for i in range(len(mas_y)):
        mas.append(mas_y[i] - mas_y[i-1])
        
    mas.pop(0)  
    if j == 1:
        return mas
    else:
        j-=1
        return y(mas, j)
yx1=1/h*((y(mas_y, 1)[1])-(y(mas_y, 2)[1])/2+(y(mas_y, 3)[1])/3-(y(mas_y, 4)[1])/4)
yx2=1/h**2*((y(mas_y, 2)[1])-(y(mas_y, 3)[1])+11/12*(y(mas_y, 4)[1]))

q=(x-xn)/h
Nx1=mas_y[0]+q*mas_y[1]-mas_y[0]
print ("Напишите порядок до которого будет работать подсчёт")
jkl=int(input())-1

while k<jkl:
    k+=1
    Nx1+=(q*(fac1(k, q))/math.factorial(k+1))*(y(mas_y,k+1)[0])
N1= mas_y[0] + q*mas_y[1]-mas_y[0]+(q*(q-1)/math.factorial(2))*(y(mas_y, 2)[0]) + (q*(q-1)*(q-2)/math.factorial(3))*(y(mas_y, 3)[0])

k=0
Nx2=mas_y[jkl]+q*mas_y[1]-mas_y[0]
while k<jkl:
    k+=1
    Nx2+=(q*(fac2(k, q))/math.factorial(k+1))*(y(mas_y,k+1)[jkl-k])

print ("1 інтерполяційна  формула Ньютона: //", Nx1, " // (через цыкл до)", jkl," -----------------------------------------")
print ("1 інтерполяційна  формула Ньютона: //", N1," // (через Формулу до 3 порядка) --------------------------------------")
print ("2 інтерполяційна  формула Ньютона: //", Nx2, " // (через цыкл до)", jkl," -----------------------------------------")
plt.plot(mas_x, mas_y, label='Nx1 , Nx2')
plt.title('LB_9 Ostranytsia Dmytro')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()