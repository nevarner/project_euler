"""Problem 1 on ProjectEuler.net"""


"""If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

def problem_1(n: int = 1000) -> int:
    """The sum of numbers below 1000 which are divisible by 3 is the same
    as 3 times the sum of numbers from 1 to (1000//3). Similarly for 5 and 15.
    If we sum the multiples of 3 and the multiples of 5, we add the
    sum of multiples of the least common multiple of 3 and 5 (i.e, 15) twice,
    so we can subtract the extra sum of multiples of 15 to get the right
    answer."""
    def sum_to_n(n: int) -> int:
        """Sum from 1 to n is half of n+1 added together n times."""
        return n*(n+1)//2

    n3 = (1000-1)//3
    n5 = (1000-1)//5
    n15 = (1000-1)//15
    res = 3*sum_to_n(n3) + 5*sum_to_n(n5) - 15*sum_to_n(n15)
    return res


print(problem_1())
