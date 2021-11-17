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
                        type= str  ,
                        help='DNA text or file')
    args = parser.parse_args()
    if os.path.isfile(args.text):
         args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    #print(args)
    # dict = OrderedDict.fromkeys(input)
    prev = ''
    count = 0
    for base in args.text :
        print(base, base == prev)
        prev = base
        if base == prev:
            count += 1
            print(count)
        else:
            count = 1
            print(base)
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
if __name__ == '__main__':
    main()
