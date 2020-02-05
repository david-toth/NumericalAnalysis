## Secant Method
## Numerical Analysis 10e by
## Burden, Burden, and Faires

from math import log, exp, sin, cos, tan, pi, e

def SecantMethod(p0, p1, tol, N):

    f_in = input("Enter function, f: ")
    f = eval("lambda x:" + f_in)

    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= N:

        p = p1 - q1*(p1 - p0)/(q1 - q0)

        if abs(p - p1) < tol:
            return p

        i = i + 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)

    print("Failed after ", N, " iterations.")
    return 
