"""
Monte Carlo estimation of Pi.

This function estimates the value of Pi by randomly sampling points in a 2x2
square and counting how many of them fall within a circle of radius 1 centered
at the origin. The ratio of points inside the circle to the total number of
points is an approximation of Pi/4.

Time Complexity: O(n), where n is the number of samples.
Space Complexity: O(1)
"""
import random

def monte_carlo_pi(samples: int = 1000) -> float:
    """
    Estimate the value of Pi using a Monte Carlo simulation.

    Args:
        samples: The number of random points to sample.

    Returns:
        An estimation of the value of Pi.
    """
    inside = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x * x + y * y <= 1:
            inside += 1
    return 4 * inside / samples

if __name__ == "__main__":
    pi_estimate = monte_carlo_pi(100000)
    print(f"Estimated value of Pi: {pi_estimate}")