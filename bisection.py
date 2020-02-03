## Bisection method for finding roots
## Numerical Analysis


def bisection(f, a, b, tol, iters):

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
    
    return None 

        
