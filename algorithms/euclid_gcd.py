"""Euclid's algorithm for greatest common divisor (GCD).

Repeatedly replaces the larger number with the remainder until zero is reached.
Time Complexity: O(log min(a, b))
Space Complexity: O(1)
"""

def euclid_gcd(a, b):
    """Return the greatest common divisor of *a* and *b*."""
    while b:
        a, b = b, a % b
    return a
