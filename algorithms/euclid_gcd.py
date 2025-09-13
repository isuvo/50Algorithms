"""Euclid's algorithm for greatest common divisor (GCD).

Repeatedly replaces the larger number with the remainder until zero is reached.
Time Complexity: O(log min(a, b))
Space Complexity: O(1)
"""

def euclid_gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of *a* and *b*."""
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    num1 = 48
    num2 = 18
    gcd = euclid_gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {gcd}")