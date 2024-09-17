import numpy as np
from typing import Tuple

def thomas(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solve a tridiagonal system of linear equations using the Thomas
    algorithm.

    The Thomas algorithm is an optimized method for solving tridiagonal linear
    systems of the form A * z = b, where A is a tridiagonal matrix. This
    algorithm is a specific form of Gaussian elimination and has a
    computational complexity of O(n), making it efficient for large systems.

    Parameters
    ----------
    A : np.ndarray
        A tridiagonal, invertible square matrix of shape (n, n).
    b : np.ndarray
        A constant matrix (column vector) of shape (n,).

    Returns
    -------
    np.ndarray
        Solution vector `z` of shape (n,), representing the solution of the
        linear system A * z = b.

    Raises
    ------
    ValueError
        If 'A' is not a square matrix or if 'A' and 'b' do not have compatible
        dimensions.

    Notes
    -----
    - The input matrix `A` must be strictly tridiagonal.
    - This method assumes that the matrix `A` is invertible.
    """
    # Copy the right-hand side vector to avoid modifying the input
    d_n: np.array = b.copy()
    
    # Get the dimensions of matrix A
    n: Tuple[int, int] = A.shape

    # Initial validation checks
    if n[0] != n[1]:
        raise ValueError("'A' must be a square matrix.")
    elif n[0] != b.size:
        raise ValueError("'A' and 'b' must be the same size.")

    # Extract the coefficients from matrix A
    # 'a_n' is the sub-diagonal (lower diagonal)
    a_n: np.ndarray = np.pad(np.diag(A, -1), (1,))
    
    # 'b_n' is the main diagonal
    b_n: np.ndarray = np.diag(A, 0)
    
    # 'c_n' is the super-diagonal (upper diagonal)
    c_n: np.ndarray = np.pad(np.diag(A, 1), (0, 2))

    # Arrays to hold the modified coefficients for the forward sweep
    p_i: np.ndarray = np.zeros(b.size)
    q_i: np.ndarray = np.zeros(b.size)

    # Forward sweep for the Thomas algorithm
    p_i[0] = c_n[0] / b_n[0]
    q_i[0] = d_n[0] / b_n[0]

    # Iterate through the matrix rows to modify coefficients
    for i in range(1, n[0]):
        denom = b_n[i] - p_i[i - 1] * a_n[i]
        p_i[i] = c_n[i] / denom
        q_i[i] = (d_n[i] - q_i[i - 1] * a_n[i]) / denom

    # Back-substitution step to find the solution vector 'z'
    z: np.ndarray = np.zeros(b.size)
    z[-1] = q_i[-1]

    # Iterate backwards to find the remaining elements of 'z'
    for i in range(-2, -n[0] - 1, -1):
        z[i] = q_i[i] - p_i[i] * z[i + 1]

    return z

def main():
    # Define the tridiagonal matrix A
    A = np.array([[-2.6,  1.0,  0.0,  0.0],
                  [ 1.0, -2.6,  1.0,  0.0],
                  [ 0.0,  1.0, -2.6,  1.0],
                  [ 0.0,  0.0,  1.0, -2.6]])
    
    # Define the right-hand side vector b
    b = np.array([-240.0, 0.0, 0.0, -150.0])

    # Solve the system using the Thomas algorithm
    print(thomas(A, b))


if __name__ == '__main__':
    main()
