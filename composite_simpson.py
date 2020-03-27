from math import *

def composite_simpson():

    f_in = input("Enter f: ")
    f = eval("lambda x:" + f_in)

    n = int(input("Enter n: "))

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    h = (b-a)/n
    XI0 = f(a) + f(b)
    XI1 = 0
    XI2 = 0

    for i in range(1, n):

        X = a + i*h
        if i % 2 == 0:
            XI2 += f(X)

        else:
            XI1 += f(X)

    XI = (h/3)*(XI0 + 2*XI2 + 4*XI1)

    print(XI)

composite_simpson()
