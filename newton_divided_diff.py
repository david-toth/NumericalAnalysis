# Newton's Divided-Difference

import numpy as np

def NewtonDD(x,f):

    n = len(x)
    F = np.zeros((n,n))

    F[:,0] = f
    print(F)
    for i in range(1,n):

        for j in range(1,i+1):

            F[i,j] = (F[i,j-1] - F[i-1,j-1]) / (x[i] - x[i-j])


    coefs = np.diagonal(F)

    return coefs
