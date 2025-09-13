import math
import random

def simulated_annealing(f, x0, temp=1.0, cooling=0.95, iterations=100):
    """Minimize function f using simulated annealing.

    Time: O(iterations), Space: O(1)
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
