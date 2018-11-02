import os

from parser import parse_system
from argparser import argparser
from simulation import EdfScheduler, simulate

SYSTEM_FILE = os.path.join(os.path.dirname(__file__), 'data/system.txt')


def main():
    args = argparser.parse_args()
    print(args)
    tasks = parse_system(SYSTEM_FILE)
    scheduler = EdfScheduler()
    simulate(scheduler, tasks, 0, 20)


if __name__ == "__main__":
    main()
