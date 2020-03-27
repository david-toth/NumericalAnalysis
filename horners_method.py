# Horner's Method

from math import *

def Horner(n, coefs, x0):

    y = coefs[-1]
    z = coefs[-1]

    for j in range(n-1, 0, -1):

        y = x0*y + coefs[j]
        z = x0*z + y

    y = x0*y + coefs[0]

    print("y = P(x0) = ", y)
    print("z = P'(x0) = ", z)

    
Horner(3, [-1,1,-2,3],2)
