import cmath


def fft(x):
    """Compute the discrete Fourier transform using the Cooley-Tukey FFT.

    Length of x must be a power of two.
    Time: O(n log n), Space: O(n)
    """
    n = len(x)
    if n == 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    factor = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + factor[k] for k in range(n // 2)] + [even[k] - factor[k] for k in range(n // 2)]
