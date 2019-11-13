# -*- coding: utf-8 -*-
import numpy as np
from thomas import *


def edo2(p, q, f, h, a, b, y0, yn):
    """
    Inputs
    
    @p - function p

    @q - function q

    @f - function f

    @h - step

    @a - initial value

    @b - final value
    
    @y0 - initial value y(a)

    @yn - end value y(b)

    Outputs
    @x - vector x
    
    @y - vector y
    """
    x = np.arange(a, b, h)
    # Create Linear System Equation Ax = v
    # Compute diagonals values
    diagonal0 = 2 + q(x[1:-1])*h**2
    diagonal_1 = -p(x[2:-1])*h/2 - 1
    diagonal1 = p(x[1:-2])*h/2 - 1
    # Tridiagonal matriz
    A = np.diag(diagonal_1, -1) + np.diag(diagonal0, 0) + np.diag(diagonal1, 1)
    # Constants
    # y0 = alpha, yn = beta
    e0 = (p(x[1])*h/2 + 1)*y0
    eN = (-p(x[-2])*h/2 + 1)*yn
    # Vector
    v = -f(x[1:-1])*h**2
    v[0] += e0
    v[-1] += eN
    # Solving Linear System Equation
    y = thomas(A, v)
    y = np.append(np.append(y0, y), yn)
    return x, y

if __name__ == '__main__':
    print('Finite Difference method working, put your code below')
    p = lambda x: -1/x
    q = lambda x: 1/(4*x**2) - 1
    f = lambda x: 0*x

    h = 0.1
    a = 1
    b = 6
    y0 = 1
    yn = 0

    xAprox, yAprox = edo2(p, q, f, h, a, b, y0, yn)
    print(xAprox)
    print(yAprox)
