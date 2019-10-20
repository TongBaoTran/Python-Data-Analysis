# [] list
# () tuple
"""
The empty tuple is written as two parentheses containing nothing −
tup1 = ();
To write a tuple containing a single value you have to include a comma, even though there is only one value −
tup1 = (50,);

"""

# Cannot change value of tuple
from math import *
from typing import Tuple

solution=[0]*2


def solve_quadratic(a, b, c):
    solution[0]=(-b + sqrt(b ** 2 - 4 * a * c)) / 2 / a
    solution[1]=(-b - sqrt(b ** 2 - 4 * a * c)) / 2 / a
    return tuple(solution)


print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 1))