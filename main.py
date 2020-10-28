import sys
import argparse
from logic_hammer import LogicHammer


def main():
    parser = argparse.ArgumentParser(description='Just stupid')
    parser.add_argument('--path-in', type=str, help='Input path')
    parser.add_argument('--path-out', type=str, help='Output path')

    args = parser.parse_args()

    hammer = LogicHammer(args.path_in)
    if args.path_out is None:
        print(hammer)
    else:
        open(args.path_out, 'w').write(str(hammer))


if __name__ == '__main__':
    main()
