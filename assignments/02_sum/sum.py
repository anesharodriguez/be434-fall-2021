#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nums',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='numbers to add')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='rejected')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)
   # parser.add_argument('reject',
   #                     metavar='str',
    #                    nargs='+',
     #                   help= 'need number')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num_arg = args.num
    NumList = []
    number = int(input("Enter how many numbers:"))

    for i in range(1, number + 1):
        value = int(input("Enter the number:"))
        NumList.append(value)
        total = sum(NumList)
        print("sum:",total)
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
