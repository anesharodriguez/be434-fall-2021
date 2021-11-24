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
                        nargs='+',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='File',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # for pattern in args.pattern:
    #     print(pattern, end='\n')

    num_files = len(args.file)
    for fh in args.file:
        for line in fh:
            if re.search(args.pattern, line,
                         re.IGNORECASE if args.insensitive else 0):
                args.outfile.write('{}{}'.format(
                    f'{fh.name}:' if num_files > 1 else '', line))
                    
                # print(line, end='', file=args.outfile)
            # else:
            #     if re.search(args.pattern, line):
            #         print(line, end='', file=args.outfile)
        # for line in fh:
        #     if re.search(sys.argv[1], line):
        #         print(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
