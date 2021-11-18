#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-11-16
Purpose: Rock the Casbah
"""

import argparse
import os
from typing import Sequence


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type=str,
                        help='DNA text or file')
    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # print(args)
    # dict = OrderedDict.fromkeys(input)
    # prev = ''
    # total_base = 0
    for base in args.text.splitlines():
        print(rle(base))
    #     print(base, base == prev)
    #     prev = base
    #     count = 0
    #     if base == prev:
    #         count += 1
    # total_base += count
    # print(total_base)
        # else:
        # print(base)

        # patrn.append(line.rstrip())
        # if text == os.path.isfile:
        #     open('readme.txt').readlines()
        # else:
        #      print(text, end='')
        # for letter, value in dict.items():
        # for base in line:

    #          for i in len(base):
    #              base = base[i] + 1
    # #     for line in fh:

        #print(base, line, end='')

# --------------------------------------------------


def rle(text: str) -> str:
    """Run-length encoding"""
    prev = ''
    count = 1
    counts = []
    for char in text:
        if char == prev:
            count += 1
            # print(count)
        else:
            counts.append((prev, count))
            count = 1
            prev = char

    counts.append((prev, count))
    # print(counts)

    ret = ''
    for char, count in counts:
        ret += '{}{}'.format(char, count if count > 1 else '')

    return ret

# --------------------------------------------------


def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()
