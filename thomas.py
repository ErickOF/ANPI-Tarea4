def thomas(A, b):
    """ Thomas Method implementation in Python.

        Thomas Method is a linear algebra numerical algorith that solves a
        linear equation system A*z = b efficiently.

        Parameters
        ----------
        A : matrix
            Tridiagonal, invertible matrix.
        b : list
            Constant matrix (column vector) as a list.

        Returns
        ----------
        z : list
            Solution matrix (column vector) as a list.

        Raises
        ------
        ValueError
            If A is not a square matrix or 'A' and 'b' are not the same size.
    """

    # Initial validations
    n = len(A)
    if (n != len(A[0])):
        raise ValueError("'A' must be a square matrix.")
    elif(n != len(b)):
        raise ValueError("'A' and 'b' must be the same size.")
    else:
        # Extract coefficients from matrix A
        a_n = [0] * len(A)
        b_n = [0] * len(A)
        c_n = [0] * len(A)

        for i in range(0, len(A)):
            b_n[i] = A[i][i]

        for i in range(1, len(A)):
            a_n[i] = A[i][i - 1]

        for i in range(0, len(A) - 1):
            c_n[i] = A[i][i + 1]

        # Modify coefficients
        c_n[0] /= b_n[0]
        b[0] /= b_n[0]

        for i in range(1, n):
            p_i = b_n[i] - (a_n[i] * c_n[i - 1])
            c_n[i] /= p_i
            b[i] = (b[i] - a_n[i] * b[i - 1])/p_i

        # Back-Substitution Method
        z = [0 for i in range(n)]
        z[-1] = b[-1]

        for i in range(-2, -n - 1, -1):
            z[i] = b[i] - c_n[i] * z[i + 1]

        return z

# =================== FOR TESTING, REMOVE AFTER TESTING ======================


def main():
    A = [[-2.6, 1, 0, 0], [1, -2.6, 1, 0],
         [0, 1, -2.6, 1], [0, 0, 1, -2.6]]
    b = [-240, 0, 0, -150]

    print(thomas(A, b))


if __name__ == '__main__':
    main()
