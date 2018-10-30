import os
import argparse

from parser import parse_system

SYSTEM_FILE = os.path.join(os.path.dirname(__file__), 'data/system.txt')


def main():
    system_description = parse_system(SYSTEM_FILE)
    print(system_description)


main()
