# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from edo2 import *


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
            ax.plot(x[i % N], y[i % N])
        else:
            ax.plot(x[i % N], y[i % N], '--')
        ax.legend(legends[:(i % N) + 1])
    anim = FuncAnimation(fig, update, frames=np.arange(0, 10*len(x), 1), interval=500, repeat=True, save_count=200)
    anim.save('finite_difference_method.gif', fps=1)


if __name__ == "__main__":
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
        legends.append('Aprox h={}'.format(h))
        x.append(xAprox)
        y.append(yAprox)

    x.insert(0, x[0])
    y.insert(0, yReal(x[0]))
    legends.insert(0, 'Real')

    plot(x, y, legends)
