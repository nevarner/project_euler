"""Problem 7 on ProjectEuler.net"""


def is_prime(m: int) -> bool:
    """Checks if m is prime"""
    m_max = int(m ** .5)
    for i in range(m_max, 1, -1):
        if m % i == 0:
            return False
    return True


def problem_7(n: int=10_001) -> int:
    """Returns the nth prime"""
    count = 1
    i = 3
    while count < 10_001:
        if is_prime(i):
            count += 1
        if count == 10_001:
            return i
        i += 1
