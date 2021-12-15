"""Problem 4 on ProjectEuler.net"""


import numpy as np


def problem_4():
    """Largest number most likely starts and ends with a 9, so try digits
    ending in 3."""
    def is_palendrome(num):
        s = str(num)
        l = len(s) - 1
        res = []
        for i, _ in enumerate(s[:3]):
            res.append(s[i] == s[l - i])
        return all(res)

    for x1 in np.arange(993, 102, -10):
        for x2 in np.arange(993, 102, -10):
            if is_palendrome(x1 * x2):
                return x1, x2, x1 * x2
