"""Sieve of Eratosthenes for generating primes up to n.

Marks multiples of each prime starting from 2.
Time Complexity: O(n log log n)
Space Complexity: O(n)
"""

def sieve_of_eratosthenes(n):
    """Return a list of all prime numbers less than or equal to *n*."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, prime in enumerate(sieve) if prime]
