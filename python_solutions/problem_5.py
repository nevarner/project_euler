"""Problem 5 on ProjectEuler.net"""


def problem_5(max_: int=20):
    """We move up through i in range(2, max_+1). We keep a list of primes l.
    If i is prime, we add it to l. If i is not prime, try to evenly divide it
    by the other elements in l and add the resulting number to l if it isn't
    1. This list consists of the prime factors of the desired number, so
    we return the product of the primes in the list."""
    n, l = 1, []
    for i in range(2, max_+1):
        j = i
        for k in l:
            if j % k == 0:
                j //= k
        if j != 1:
            l.append(j)
        n *= j
    return n
