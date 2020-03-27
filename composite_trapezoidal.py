from math import *
import numpy as np

def composite_trap():

    f_inp = input("Enter function: ")
    f = eval("lambda x:" + f_inp)

    n = int(input("Enter n: "))

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    h = (b - a)/n

    xj_sum = 0

    for j in range(1,n):

        x = a + j*h
        xj_sum += f(x)

    print('\n')

    print(0.5*(f(a) + 2*xj_sum + f(b)))

composite_trap()
    

    
