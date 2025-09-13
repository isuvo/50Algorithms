"""
Gradient descent optimization algorithm.

This implementation of gradient descent finds the minimum of a single-variable
function. It iteratively moves in the direction of the negative gradient of
the function to find the local minimum.

Time Complexity: O(i), where i is the number of iterations.
Space Complexity: O(1)
"""
from typing import Callable

def gradient_descent(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    lr: float = 0.1,
    iterations: int = 100,
) -> tuple[float, float]:
    """
    Perform gradient descent on a scalar function f.

    Args:
        f: The function to minimize.
        df: The derivative of the function f.
        x0: The initial point.
        lr: The learning rate.
        iterations: The number of iterations to perform.

    Returns:
        A tuple containing the point at which the minimum is found and the
        value of the function at that point.
    """
    x = x0
    for _ in range(iterations):
        x -= lr * df(x)
    return x, f(x)

if __name__ == "__main__":
    # Minimize the function f(x) = x^2 - 4x + 4
    def f(x: float) -> float:
        return x**2 - 4 * x + 4

    def df(x: float) -> float:
        return 2 * x - 4

    x0 = 0.0
    min_x, min_val = gradient_descent(f, df, x0)
    print(f"The minimum of the function is at x = {min_x:.2f} with a value of {min_val:.2f}")