## Fixed-Point Iteration
## Numerical Analysis 10e by
## Burden, Burden, and Faires

from math import exp, log, sin, cos, tan, pi, e

def fixedPoint(p0, tol, max_iter):
    """
    
    p0       : initial estimate
    tol      : tolerance of error
    max_iter : maximum number of iterations
        
    """

    f_inp = input("Enter the function: ")
    f = eval("lambda x:" + f_inp)
    
    i = 1

    print("i", "p", sep='\t')
    
    while i <= max_iter:

        p = f(p0)

        print(i, p, sep='\t')

        if abs(p - p0) < tol:
            return p

        p0 = p

        i += 1

    print("Method failed after ", max_iter, " iterations.")

    return

        
