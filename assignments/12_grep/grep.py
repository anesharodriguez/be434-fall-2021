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
                        help='Search pattern')

    parser.add_argument('file',
                        help='Input file(s)',
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
    with open(sys.args[2],"r") as file:
        for line in file:
            if re.search(sys.args[1], line):
                print(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
