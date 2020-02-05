## Newton's Method
## Numerical Analysis 10e by
## Burden, Burden, and Faires

from math import log, exp, cos, sin, tan, pi, e

def NewtonMethod(p0, tol, N):

    f_inp = input("Enter function, f: ")
    f = eval("lambda x:" + f_inp)

    f_prime_in = input("Enter function, f': ")
    f_prime = eval("lambda x:" + f_prime_in)

    i = 1

    while i <= N:

        p = p0 - (f(p0)/f_prime(p0))

        if abs(p - p0) < tol:
            return p

        i = i + 1
        p0 = p

    print("Failed after ", N, " iterations.")
    return 
