"""Problem 6 on ProjectEuler.net"""


def problem_6(n: int=100) -> int:
    """The sum of 1 to n is n*(n+1)//2, and the sum of 1**2 to n**2 is
    n*(n+1)*(2*n+1)//6, we just return the difference of the two."""
    sum_of_squares = n*(n+1)*(2*n+1)//6
    square_of_sum = (n*(n+1)//2)**2
    return square_of_sum - sum_of_squares
