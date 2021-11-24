import numpy as np

print("Gauss")
a = np.matrix([ [3, -5, 3], [1, 2, 1], [2, 7, -1] ])
b = np.matrix([[1], [4], [8]])
print ("Matrix A = ", a)
print ("\nMatrix b = ", b)
def fun():
    k = 1
    n = len(b)
    while k<=n-1:
        i = k+1
    while i<n:
        if a[i,k]!=0.0:
            a[i,k+1:n] = a[i,k+1:n] - (a[i,k]/a[k,k])*a[k,k+1:n]
            b[i] = b[i] - (a[i,k]/a[k,k])*b[k]
            i += 1
            k += 1
            k = n-1
    while k > -1:
        b[k] = (b[k] - np.dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
        k-=1
    return b
print ("\nGauss: ", fun())
print("\nCheck Gauss solution: ", np.linalg.solve(a,b))
print("\nJordan", np.linalg.inv(a)*b)
import numpy as np
print("Gauss")
a = np.matrix([ [3, -5, 3], [1, 2, 1], [2, 7, -1] ])
b = np.matrix([[1], [4], [8]])
print ("Matrix A = ", a)
print ("\nMatrix b = ", b)
def fun():
    k = 1
    n = len(b)
    while k<=n-1:
        i = k+1
        while i<n:
            if a[i,k]!=0.0:
                a[i,k+1:n] = a[i,k+1:n] - (a[i,k]/a[k,k])*a[k,k+1:n]
                b[i] = b[i] - (a[i,k]/a[k,k])*b[k]
                i += 1
                k += 1
                k = n-1
                while k > -1:
                    b[k] = (b[k] - np.dot(a[k,k+1:n], b[k+1:n]))/a[k,k]
                    k-=1
                    return b
print ("\nGauss: ", fun())
print("\nCheck Gauss solution: ", np.linalg.solve(a,b))
print("\nJordan", np.linalg.inv(a)*b)