import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation
from typing import Callable, List

from edo2 import edo2


def plot(
    x: List[np.ndarray],
    y: List[np.ndarray],
    legends: List[str]
) -> None:
    """
    Creates an animated plot comparing multiple approximations and the real
    solution.

    This function uses Matplotlib to create an animated plot that compares the
    solutions of a differential equation obtained through the finite
    difference method with different step sizes. It plots these solutions
    along with the real solution (if provided) to visualize the accuracy of
    the numerical method.

    Parameters
    ----------
    x : List[np.ndarray]
        A list of x-coordinates for each approximation and the real solution.
    y : List[np.ndarray]
        A list of y-coordinates corresponding to the x-coordinates for each
        approximation and the real solution.
    legends : List[str]
        A list of legend labels for each plotted line.

    Returns
    -------
    None
        This function does not return anything. It saves an animated GIF of
        the plot named 'finite_difference_method.gif'.

    Notes
    -----
    - The function animates the plot, showing each approximation one by one.
    - The final animated plot is saved as 'finite_difference_method.gif'.
    """
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()
    fig.set_tight_layout(True)

    def update(i: int):
        """
        Update function for the animation. It clears and redraws the plot at each frame.

        Parameters
        ----------
        i : int
            The current frame index.
        """
        N: int = len(x)

        if (i % N == 0):
            # Clear the plot at the beginning of each cycle
            ax.clear()
            plt.title('Finite Difference Method')
            plt.xlabel('x')
            plt.ylabel('y')
            # Plot the first line (usually the real solution)
            ax.plot(x[i % N], y[i % N])
        else:
            # Plot the current approximation with dashed lines
            ax.plot(x[i % N], y[i % N], '--')

        # Update the legend to show lines plotted up to this frame
        ax.legend(legends[:(i % N) + 1])

    # Create the animation
    anim: FuncAnimation = FuncAnimation(
        fig,
        update,
        frames=np.arange(0, 10 * len(x), 1),
        interval=500,
        repeat=True,
        save_count=200
    )

    # Save the animation as a GIF file
    anim.save('finite_difference_method.gif', fps=1)

if __name__ == "__main__":
    # Finite Difference Method Test
    # Define the coefficient functions and the real solution
    p: Callable[[float], float] = lambda x: -1 / x
    q: Callable[[float], float] = lambda x: 1 / (4 * x**2) - 1
    f: Callable[[float], float] = lambda x: 0 * x

    # Define the interval and boundary conditions
    a: float = 1.0
    b: float = 6.0
    y0: float = 1.0
    yn: float = 0.0

    # Define the real solution (for comparison purposes)
    yReal: Callable[[float], float] = lambda x: np.sin(6 - x) /\
                                                (np.sin(5) * np.sqrt(x))

    # Initialize lists to store the solutions and legends
    legends: List[str] = []
    x: List[np.ndarray] = []
    y: List[np.ndarray] = []

    # Compute the numerical solutions with different step sizes
    for i in range(1, 4):
        h: int = 10**-i
        xAprox, yAprox = edo2(p, q, f, h, a, b, y0, yn)
        legends.append('Aprox h={}'.format(h))
        x.append(xAprox)
        y.append(yAprox)

    # Insert the real solution at the beginning of the lists for comparison
    x.insert(0, x[0])
    y.insert(0, yReal(x[0]))
    legends.insert(0, 'Real')

    # Call the plot function to create and save the animated plot
    plot(x, y, legends)
