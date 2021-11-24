from numpy import *
import matplotlib.pyplot as plt
def sd(x):
    return 15*sin(10*x)*cos(3*x)
x = linspace(0, 3, 51)
y = sd(x)
plt.plot(x, y, 'g--', label='15*sin(10*x)*cos(3*x')
plt.title('LB_7.0 Ostranytsia Dmytro')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()