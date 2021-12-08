#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse
from os import remove, replace


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('num',
                        metavar='INT',
                        type=int,
                        nargs='+',
                        help='numbers to add')

  

    #parser.add_argument('reject',
     #                   metavar='str',
      #                  type=str,
     #                   nargs='+',
  #                      help= 'need number')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num = args.num
    #snum = str(num)
    for i in range(len(args.num)):
        if len(args.num) == 1:
            print(num, '=' ,args.num)
        else:
            print( str(args.num[0]),' + ', str(args.num[i]),' = ',sum(args.num))
            #print('{} + {}  = {}' .format(num) + str(num),sum(num))  
   


# --------------------------------------------------
if __name__ == '__main__':
    main()
