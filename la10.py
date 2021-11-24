import numpy as np
from numpy import *
import math
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
mas_x=[0, 1.4, 2.3, 3.3, 4.5]
mas_y=[1, 1.155, 0.079, -1.145, -1.188]
def funk_h(mas_x):
    h=[]
    i=0
    while i<=len(mas_y)-2:
        h.append(mas_x[i+1] - mas_x[i])
        i+=1
    return h
def funk_k(mas_y, H):
    k=[] 
    i=2
    while i < len(mas_y):
        k.append(3*((mas_y[i]-mas_y[i-1])/H[i-1]-(mas_y[i-1]-mas_y[i-2])/H[i-2]))
        i+=1
    return k
def funk_m(H):
    m=[]
    i=1
    while i < len(mas_y)-1:
        m.append(2*(H[i-1]+H[i]))
        i+=1
    return m
def funk_asbcd(k,m,h,y):
    i=0
    a=[0, (k[i]/m[i])]
    sb=[0, (h[i+1]/m[i])]
    c=[0]
    d=[]
    b=[]
    while i < len(mas_y)-3:
        a.append((k[i+1]-h[i+1]*a[i+1])/(m[i+1]-h[i+1]*sb[i+1]))
        sb.append(h[i+2]/(m[i+1]-h[i+1]*sb[i+1]))
        i+=1
    i=len(mas_y)-2
    while i >= 0:
        c.insert(0, a[i]-sb[i]*c[0])
        i-=1
    i=0
    while i < len(mas_y)-1:
        d.append((c[i+1]-c[i])/(3*h[i]))
        i+=1
    i=0
    while i < len(mas_y)-1:
        b.append((y[i+1]-y[i])/h[i]-(c[i+1]+2*c[i])*h[i]/3)
        i+=1
    i=0
    s=[]
    while i<len(mas_y)-1:
        s.append(a[i]+b[i]*(x-mas_x[i])+c[i]*(x-mas_x[i])+d[i]*(x-mas_x[i])**3)
        i+=1
    print ("S --",s)
    print ("B --",b)
    print ("D --",d)
    print ("C --",c)
    print ("A --",a)
    print ("SB--",sb)
    return a, sb, c, d, b
i = 0
x = 0
while i <= 4:
    x += mas_x[i]
    i += 1
x = x / 5
print ("X",x)
print("H",funk_h(mas_x))
print("K",funk_k(mas_y,funk_h(mas_x)))
print("M",funk_m(funk_h(mas_x)))
funk_asbcd(funk_k(mas_y,funk_h(mas_x)),funk_m(funk_h(mas_x)),funk_h(mas_x),mas_y)
spl = UnivariateSpline(mas_x, mas_y)
xs = linspace(0, 4.5, 1000)
plt.plot(mas_x, mas_y, 'ro', xs, spl(xs), 'g')
plt.title('LB_9 Ostranytsia Dmytro')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()