# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Thomas Algorithm
def thomas(A, b):
    return np.linalg.solve(A, b)

# Finite Difference Method
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

    @yn - end value y(n)

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

# Finite Difference Method Test
p = lambda x: -1/x
q = lambda x: 1/(4*x**2) - 1
f = lambda x: 0*x

a = 1
b = 6
y0 = 1
yn = 0

yReal = lambda x: np.sin(6 - x) / (np.sin(5) * np.sqrt(x))

legends = []
x, y = [], []
for i in range(1, 4):
    h = 10**-i
    xAprox, yAprox = edo2(p, q, f, h, a, b, y0, yn)
    legends.append(f'Aprox h={h}')
    x.append(xAprox)
    y.append(yAprox)

x.insert(0, x[0])
y.insert(0, yReal(x[0]))
legends.insert(0, 'Real')

def plot(x, y, legends):
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)
    def update(i):
        N = len(x)
        if (i % N == 0):
            ax.clear()
            plt.title('Finite Difference Method')
            plt.xlabel('x')
            plt.ylabel('y')
            ax.plot(x[i%N], y[i%N])
        else:
            ax.plot(x[i%N], y[i%N], '--')
        ax.legend(legends[:(i)%N + 1])
    anim = FuncAnimation(fig, update, frames=np.arange(0, 10*len(x), 1), interval=500, repeat=True, save_count=200)
    anim.save('finite_difference_method.gif', fps=1)

plot(x, y, legends)
