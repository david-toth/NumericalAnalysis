# Hermite Interpolation

import numpy as np

def Hermite(x, f, fp):

    n = len(x)
    z = np.zeros(2*n)
    Q = np.zeros((2*n, 2*n))

    for i in range(n):

        z[2*i] = x[i]
        z[2*i + 1] = x[i]
        Q[2*i, 0] = f[i]
        Q[2*i + 1, 0] = f[i]
        Q[2*i + 1, 1] = fp[i]

        if i != 0:

            Q[2*i,1] = (Q[2*i,0] - Q[2*i - 1,0]) / (z[2*i] - z[2*i - 1])

    for i in range(2,2*n):

        for j in range(2,i+1):

            Q[i,j] = (Q[i, j-1] - Q[i-1,j-1]) / (z[i] - z[i-j])

    coefs = np.diagonal(Q)

    return coefs
