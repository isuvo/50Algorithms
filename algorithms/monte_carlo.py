import random

def monte_carlo_pi(samples=1000):
    """Estimate pi via Monte Carlo simulation.

    Time: O(n), Space: O(1)
    """
    inside = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / samples
