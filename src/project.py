import os

from parser_ import parse_system
from argparser import argparser
from simulation import EdfScheduler, simulate


def main():
    args = argparser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
