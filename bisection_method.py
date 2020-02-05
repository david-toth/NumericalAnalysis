## Bisection Method
## Numerical Analysis 10e by
## Burden, Burden, and Faires

from math import log, exp, cos, sin, tan, pi

def bisection(a, b, tol, iters):
    
    """
    a     :   lower bound of interval
    b     :   upper bound of interval
    tol   :   error tolerance
    iters :   max number of iterations

    """

    f_inp = input("Enter the function: ")
    f = eval("lambda x:" + f_inp)

    if f(a)*f(b) > 0:
        print("Cannot work on given interval.")
        return
    
    i = 1
    FA = f(a)

    print("i", "p_n", sep='\t')
    
    while i <= iters:
        
        p = a + 0.5*(b-a)
        FP = f(p)

        print(i, p, sep='\t')
        
        if FP == 0 or 0.5*(b-a) < tol:
            return p

        if FA*FP > 0:
            a = p

        else:
            b = p
        
        i += 1
            
    print("Failed after ", iters, " iterations.")
    
    return

        
