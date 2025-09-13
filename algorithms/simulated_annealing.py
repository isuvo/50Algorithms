"""
Simulated annealing optimization algorithm.

This implementation of simulated annealing finds the global minimum of a
single-variable function. It is a probabilistic technique that approximates
the global optimum of a given function. It is inspired by the process of
annealing in metallurgy, where a material is heated and then slowly cooled to
increase the size of its crystals and reduce their defects.

Time Complexity: O(i), where i is the number of iterations.
Space Complexity: O(1)
"""
import math
import random
from typing import Callable

def simulated_annealing(
    f: Callable[[float], float],
    x0: float,
    temp: float = 1.0,
    cooling: float = 0.95,
    iterations: int = 100,
) -> tuple[float, float]:
    """
    Minimize function f using simulated annealing.

    Args:
        f: The function to minimize.
        x0: The initial point.
        temp: The initial temperature.
        cooling: The cooling rate.
        iterations: The number of iterations to perform.

    Returns:
        A tuple containing the point at which the minimum is found and the
        value of the function at that point.
    """
    x = x0
    fx = f(x)
    for _ in range(iterations):
        x_new = x + (random.random() - 0.5)
        fx_new = f(x_new)
        if fx_new < fx or math.exp((fx - fx_new) / temp) > random.random():
            x, fx = x_new, fx_new
        temp *= cooling
    return x, fx

if __name__ == "__main__":
    # Minimize the function f(x) = x^2 - 4x + 4
    def f(x: float) -> float:
        return x**2 - 4 * x + 4

    x0 = 0.0
    min_x, min_val = simulated_annealing(f, x0)
    print(f"The minimum of the function is at x = {min_x:.2f} with a value of {min_val:.2f}")