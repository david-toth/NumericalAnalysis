## Fixed-Point Iteration
## Numerical Analysis
## David Toth


def fixedPoint(g, p0, tol, max_iter):

    i = 1

    print("i", "p", sep='\t')
    
    while i <= max_iter:

        p = g(p0)

        print(i, p, sep='\t')

        if abs(p - p0) < tol:

            return p

        p0 = p

        i += 1

    print("Method failed after ", max_iter, " iterations.")

    return None

        
