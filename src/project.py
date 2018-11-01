import os
import argparse

from parser import parse_system
from simulation import EdfScheduler, simulate

SYSTEM_FILE = os.path.join(os.path.dirname(__file__), 'data/system.txt')

def main():
    tasks = parse_system(SYSTEM_FILE)
    print(tasks)
    scheduler = EdfScheduler()
    simulate(scheduler, tasks, 0, 20)

if __name__ == "__main__":
    main()
