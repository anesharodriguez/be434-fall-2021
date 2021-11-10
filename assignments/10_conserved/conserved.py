#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-11-10
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = []

    for seq in args.file:
        seqs.append(seq.rstrip())
    print('\n'.join(seqs))
    for i in range(len(seqs[0])):
        bases = []
        for sequence in seqs:
            bases += sequence[i]
        if len(set(bases)) == 1:
            print('|', end='')
        else:
            print('X', end='')

    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
