"""Exponentiation by squaring for fast power calculation.

Repeatedly squares the base and multiplies into the result when the exponent bit is 1.
Time Complexity: O(log n), where n is the exponent.
Space Complexity: O(1)
"""

def power(base: int, exponent: int) -> int:
    """Return *base* raised to *exponent* using exponentiation by squaring."""
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result

if __name__ == "__main__":
    base = 2
    exponent = 10
    result = power(base, exponent)
    print(f"{base}^{exponent} = {result}")