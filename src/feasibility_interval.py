from math import gcd
from functools import reduce
import parser_


def lcm(a, b):
    """Returns the least common multiple of a and b."""
    return a * b // gcd(a, b)


def getFeasibilityInterval(args):
    """Returns the feasibility interval of a given task system. It is computed
    as the least common multiple of all periods, plus two times the maximum
    offset.
    """
    params = vars(args)
    tasks = parser_.parse_system(params["input_file"])
    periods = [t.period for t in tasks]
    o_max = max(t.offset for t in tasks)

    interval = reduce(lcm, periods) * 2 + o_max
    print(0, interval, sep=",")
