import os
import argparse

from parser import parse_system

SYSTEM_FILE = os.path.join(os.path.dirname(__file__), 'data/system.txt')


def main():
    tasks = parse_system(SYSTEM_FILE)
    print(tasks)

if __name__ == "__main__":
    main()
