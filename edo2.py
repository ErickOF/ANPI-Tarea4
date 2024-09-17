import numpy as np

from typing import Callable, Tuple

from thomas import thomas


def edo2(
    p: Callable[[float], float],
    q: Callable[[float], float],
    f: Callable[[float], float],
    h: float,
    a: float,
    b: float,
    y0: float,
    yn: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solves a second-order differential equation using the finite difference
    method.

    This function uses the finite difference method to solve a boundary value
    problem of a second-order differential equation of the form:
    
        y'' + p(x)y' + q(x)y = f(x),
    
    on the interval [a, b] with boundary conditions y(a) = y0 and y(b) = yn.
    The interval is discretized into steps of size h.

    Parameters
    ----------
    p : Callable[[float], float]
        A function representing the coefficient of y' in the differential
        equation.
    q : Callable[[float], float]
        A function representing the coefficient of y in the differential
        equation.
    f : Callable[[float], float]
        A function representing the non-homogeneous part of the differential
        equation.
    h : float
        Step size for the finite difference discretization.
    a : float
        The initial value of the interval (start point).
    b : float
        The final value of the interval (end point).
    y0 : float
        The boundary value at the initial point, y(a).
    yn : float
        The boundary value at the final point, y(b).

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        x : np.ndarray
            The vector of discretized points in the interval [a, b].
        y : np.ndarray
            The vector of approximate solutions at the discretized points.

    Notes
    -----
    - The interval [a, b] is discretized into points with a step size of h.
    - The method creates a tridiagonal system of equations that is solved
      using the Thomas algorithm.
    """
    # Create a vector of discretized points in the interval [a, b]
    x: np.ndarray = np.arange(a, b, h)

    # Create the linear system Ax = v for the finite difference method
    # Compute the values for the diagonals of the tridiagonal matrix A
    diagonal0: np.ndarray = 2 + q(x[1:-1]) * h**2
    diagonal_1: np.ndarray = -p(x[2:-1]) * h / 2 - 1
    diagonal1: np.ndarray = p(x[1:-2]) * h / 2 - 1

    # Construct the tridiagonal matrix A using the diagonals
    A: np.ndarray = np.diag(diagonal_1, -1) + np.diag(diagonal0, 0) +\
        np.diag(diagonal1, 1)

    # Constants for boundary conditions
    # y0 = alpha, yn = beta
    e0: np.ndarray = (p(x[1]) * h / 2 + 1) * y0
    eN: np.ndarray = (-p(x[-2]) * h / 2 + 1) * yn

    # Construct the right-hand side vector v
    v: np.ndarray = -f(x[1:-1]) * h**2
    # Adjust the first element for the boundary condition at a
    v[0] += e0
    # Adjust the last element for the boundary condition at b
    v[-1] += eN

    # Solve the linear system using the Thomas algorithm
    y: np.ndarray = thomas(A, v)

    # Append the boundary values to the solution vector
    y = np.append(np.append(y0, y), yn)

    return x, y

if __name__ == '__main__':
    print('Finite Difference')

    # Example usage
    # Define the coefficient functions and boundary conditions
    p: Callable[[float], float] = lambda x: -1 / x
    q: Callable[[float], float] = lambda x: 1 / (4 * x**2) - 1
    # Homogeneous part of the equation
    f: Callable[[float], float] = lambda x: 0 * x

    # Define the interval, step size, and boundary conditions
    h: float = 0.1
    a: float = 1.0
    b: float = 6.0
    y0: float = 1.0
    yn: float = 0.0

    # Compute the approximate solution using the finite difference method
    xAprox, yAprox = edo2(p, q, f, h, a, b, y0, yn)

    print(xAprox)
    print(yAprox)
