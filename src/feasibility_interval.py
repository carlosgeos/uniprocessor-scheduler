from math import gcd
from functools import reduce
import parser_
def calcLCM(a,b):
    return a*b//gcd(a,b)


def getFeasibilityInterval():
    tasks=parser_.parse_system("./data/system.txt")
    periods=[]
    o_max=0
    for task in tasks:
        periods.append(task.period)
        if task.offset>o_max:
            o_max=task.offset

    interval=reduce(calcLCM,periods)*2+o_max
    print(0,",",interval)

getFeasibilityInterval()
