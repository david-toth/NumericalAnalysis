# Composite Midpoint

from math import *

def composite_midpoint(f,a,b,n):

    h = (b-a)/(n+2)
    x = [a+(j+1)*h for j in range(-1,n+2)]

    total = 0

    for j in range(0, int(n/2)+1):
        total += f(x[2*j + 1])

    return 2*h*total

######
f = lambda x: x*log(x)
print(composite_midpoint(f,1,2,4))
