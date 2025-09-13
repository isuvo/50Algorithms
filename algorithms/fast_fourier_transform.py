"""
Fast Fourier Transform (FFT).

This implementation of the FFT algorithm computes the discrete Fourier transform
of a sequence. It is a divide-and-conquer algorithm that recursively breaks
down the DFT into smaller DFTs. The length of the input sequence must be a
power of two.

Time Complexity: O(n log n), where n is the length of the input sequence.
Space Complexity: O(n), where n is the length of the input sequence.
"""
import cmath
from typing import List

def fft(x: List[complex]) -> List[complex]:
    """
    Compute the discrete Fourier transform using the Cooley-T_ukey FFT algorithm.

    Args:
        x: The input sequence of complex numbers. The length of x must be a
           power of two.

    Returns:
        The discrete Fourier transform of the input sequence.
    """
    n = len(x)
    if n == 1:
        return x
    if n % 2 != 0:
        raise ValueError("Length of input sequence must be a power of two")
    even = fft(x[0::2])
    odd = fft(x[1::2])
    factor = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + factor[k] for k in range(n // 2)] + [even[k] - factor[k] for k in range(n // 2)]

if __name__ == "__main__":
    # Example: FFT of a simple sequence
    x = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    y = fft(x)
    print("FFT of the sequence:")
    for c in y:
        print(f"{c.real:.2f} + {c.imag:.2f}j")