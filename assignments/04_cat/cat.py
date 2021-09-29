#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-09-28
Purpose: Rock the Casbah
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='file',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Print line numbers',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.files:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print('{:>6}\t{}'.format(line_num, line), end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
