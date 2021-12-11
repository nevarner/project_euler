"""Problem 3 on ProjectEuler.net"""


# Largest prime factor
"""Return the largest prime factor of 600851475143. The program should
work for any positive number as long as hardware allows for it."""


def problem_3(n: int = 600851475143):
    from collections import Counter
    """Recursively apply find_primes to generate a list of primes."""
    def find_primes(x: int, primes: list = None) -> list:
        """Check all possible prime divisors of x. If x is prime,
        append it to the list of primes; otherwise, if k is the largest
        divisor of x, apply find_primes to x//k and k."""
        if primes is None:
            primes = []
        n_max = int(x**.5)
        for k in range(n_max, 1, -1):
            if x % k == 0:
                find_primes(x//k, primes)
                find_primes(k, primes)
                return primes
        primes.append(x)
        return primes

    prime_list = find_primes(n)
    counted_primes = sorted(Counter(prime_list).most_common())
    res1 = f'Prime Decomposition: {counted_primes}'
    res2 = f'Largest Prime: {max(prime_list)}'
    res = res1 + '\n' + res2
    return res

print(problem_3())
