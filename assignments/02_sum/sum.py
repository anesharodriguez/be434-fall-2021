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
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('num',
                        metavar='int',
                        nargs='+',
                        help='numbers')

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
try:
    NumList = []
    number = int(input("Enter how many numbers:"))

    for i in range(1, number + 1):
        value = int(input("Enter the number:"))
        NumList.append(value)
        total = sum(NumList)
        print("sum:",total)
        assert number != int
        print('need number')
except AssertionError as msg:
    print(msg)
    
       
            
    

    
      



# --------------------------------------------------
if __name__ == '__main__':
    main()
