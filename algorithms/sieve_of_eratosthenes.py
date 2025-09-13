"""Sieve of Eratosthenes for generating primes up to n.

Marks multiples of each prime starting from 2.
Time Complexity: O(n log log n), where n is the upper limit.
Space Complexity: O(n), where n is the upper limit.
"""
from typing import List

def sieve_of_eratosthenes(n: int) -> List[int]:
    """Return a list of all prime numbers less than or equal to *n*."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, prime in enumerate(sieve) if prime]

if __name__ == "__main__":
    limit = 30
    primes = sieve_of_eratosthenes(limit)
    print(f"Prime numbers up to {limit}: {primes}")