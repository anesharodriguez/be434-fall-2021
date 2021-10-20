#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-10-18
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='SEQ',
                        nargs='+',
                        type=str,
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    base = {'A': 'A', 'C': 'C',
            'G': 'G', 'T': 'T', 'U': 'U',
            'R': '[AG]', 'Y': '[CT]', 'S': '[GC]',
            'W': '[AT]', 'K': '[GT]', 'M': '[AC]',
            'B': '[CGT]', 'D': '[AGT]', 'H': '[ACT]',
            'V': '[ACG]', 'N': '[ACGT]'}
    for seq in args.sequence:
        new_seq = ''
        for char in seq:
            new_seq += base.get(char)
        print(seq, new_seq, file=args.outfile)
    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
