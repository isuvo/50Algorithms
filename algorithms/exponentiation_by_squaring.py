"""Exponentiation by squaring for fast power calculation.

Repeatedly squares the base and multiplies into the result when the exponent bit is 1.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def power(base, exponent):
    """Return *base* raised to *exponent* using exponentiation by squaring."""
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result
