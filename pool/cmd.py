from __future__ import print_function

import argparse
import os
import sys

import pool.demo


def main():
    print(os.getcwd())
    print(os.listdir("."))
    print(os.listdir("tools"))
    parser = argparse.ArgumentParser(
        description='ball locator')
    parser.add_argument('input', type=argparse.FileType('r'))
    parser.add_argument('output', nargs='?', type=argparse.FileType('w'),
                        default=sys.stdout)

    args = parser.parse_args()
    assert args.input is not None
    assert args.output is not None
    pool.demo.demo(args.input)
    return 0


if __name__ == '__main__':
    main()