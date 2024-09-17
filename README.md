# **Instituto Tecnológico de Costa Rica**
CE3102: Numerical Analysis for Engineering

Computer Engineering

**Semester:** II - 2019  

## **Assignment 4**

### **Numerical Solution of a Differential Equation**

#### **Problem**
This assignment consists of solving the following problem.

**Problem A:** Let $y = y(x)$ be a continuous function on the interval $[a, b]$. Consider the differential equation

$$
\begin{cases}
    y'' = p(x)y' + q(x)y + f(x) \\
    y(a) = y_0, \quad y(b) = y_n
\end{cases}
$$

where $p(x)$, $q(x)$, $f(x)$ are continuous functions of real variable. We define $x_0 = a$, $x_n = b$, and a support set $S = \{x_0, x_1, ..., x_n\}$, such that $h = x_{i+1} - x_i$, for all $i = 0, 1, ..., n - 1$. The problem consists of calculating a set of points $\{(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)\}$ that numerically approximate the function $y$ in the interval $[a, b]$.

#### **Questions**

1. Implement a function named `thomas` that solves a linear system of the form $Az = b$, where $A$ is an invertible tridiagonal matrix of size $m \times m$ and $b, z$ are column vectors of size $m$. The function receives the matrix $A$ and the vector $b$ as input parameters, and the output parameter is the vector $z$ that solves the system $Az = b$.

2. Implement the finite difference method that solves Problem A. To do this, create a function named `edo2`, whose initial parameters are the functions $p$, $q$, and $f$, the step size $h$, the values $a$, $b$ of the interval, and the initial values $y_{0}$, $y_{n}$. The output parameters are the vectors $x = [x_0, x_1, ..., x_n]^T$ and $y = [y_0, y_1, ..., y_n]^T$.  

   **Note:** The function `edo2` needs to solve a system of linear equations whose coefficient matrix is a tridiagonal matrix. To solve this system, use the `thomas` function implemented in Question 1.

3. Implement a script to approximate the solution of the problem

$$
\begin{cases}
    y'' = -\frac{1}{x} y' + \left(\frac{1}{4x^2} - 1\right) y \\
    y(1) = 1, \quad y(6) = 0
\end{cases}
$$

To do this, generate an animation in which every 2 seconds a new graph appears representing an approximation of the solution to the differential equation with different values of $h$. Use the values $h = 10^{-i}$, where $i = 1, 2, ..., 10$. Additionally, at the start of the animation, the exact solution of the problem should appear:

$$
y(x) = \frac{\sin(6 - x)}{\sin(5)\sqrt{x}}.
$$

The animation should indicate a legend for each graph.
