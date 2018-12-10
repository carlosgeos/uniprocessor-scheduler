from math import gcd
from functools import reduce
import parser_

def lcm(a,b):
    return a*b//gcd(a,b)


def getFeasibilityInterval(args):
    params = vars(args)
    tasks=parser_.parse_system(params["input_file"])
    periods = [t.period for t in tasks]
    o_max = max(t.offset for t in tasks)

    interval=reduce(lcm,periods)*2+o_max
    print(0,interval,sep=",")

