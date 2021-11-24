import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import sympy as sp
x = [0.1, 0.15, 0.2, 0,3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5]
y = []
XX=0
YY=0
XX2=0
XY=0
a1=0
a0=0
i=0
while i<len(x):
    y.append(sp.sin(5*x[i]))
    i+=1
i=0
while i<(len(x)-1):
    XX+=x[i]
    YY+=y[i]
    XX2+=(x[i])**2
    XY+=x[i]*y[i]
    i+=1
XX/=len(x)
YY/=len(x)
XX2/=len(x)
XY/=len(x)
print ("X avg---",XX, "Y avg---",YY, "XY ---",XY, "XX**2 ---",XX2)
a1=XY-XX*YY/XX2-XX**2
a0=YY-a1*XX
print ("A1 --- ",a1, "A0 --- ",a0)
def F(a1, a0):
    f=a0-a1
    print ("F-", f)
    return f
xs = linspace(0, 4.5, 1000)
plt.plot(F(a1,a0), 'ro', xs)
plt.title('LB_12 Ostranytsia Dmytro')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()