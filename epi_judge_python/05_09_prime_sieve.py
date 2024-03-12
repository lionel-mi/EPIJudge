from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = []
    candidates = [False, False] + [True] * (n-1)
    for c in range(2, len(candidates)):
        if candidates[c]:
            primes.append(c)
        for cc in range(c, len(candidates), c):
            candidates[cc] = False
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('05_09_prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
