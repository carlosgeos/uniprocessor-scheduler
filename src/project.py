from argparser import argparser


def main():
    args = argparser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
