# Steffensen's Method
# Numerical Analysis 10e
# Burden, Burden, & Faires

from math import *

def Steffensen(p0, N, tol=None):

    f_in = input("Enter function: ")
    f = eval("lambda x:" + f_in)

    i = 1

    print("i", "p", sep='\t')

    while i <= N:

        p1 = f(p0)
        p2 = f(p1)
        p = p0 - ((p1 - p0)**2 / (p2 - 2*p1 + p0))

        print(i, p, sep='\t')

        if abs(p - p0) < tol:
            return p

        i = i + 1
        p0 = p

   print("Failed after ", N, " iterations.")
   return
