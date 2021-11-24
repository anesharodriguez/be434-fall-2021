#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-11-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import re
from typing import Pattern

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        type= str,
                        help='Search pattern')

    parser.add_argument('file',
                        help='Input file(s)',
                        nargs='*',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-i',
                        '--insenitive',
                        help='Case-insensitive search',
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='File',
                        help='Output',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.file:
        print(fh)
        for line in fh:
            if re.search(sys.argv[1], line):
                print(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
