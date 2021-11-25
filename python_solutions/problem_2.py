"""Problem 2 on ProjectEuler.net"""


from functools import lru_cache


@lru_cache(maxsize=3)
def fib_recursion(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


def problem_2(max_value: int = 4_000_000) -> int:
    fib_sum = 0
    i = 1
    while fib_recursion(i) <= max_value:
        if fib_recursion(i) % 2 == 0:
            fib_sum += fib_recursion(i)
        i += 1
    return fib_sum
