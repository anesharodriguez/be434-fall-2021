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
  
    print(' {}  '  .format(' + ' .join(str(num)),num),' , ' ' ' .replace, ' = ',sum(num))
   #print('{} =' .format(snum) + str(snum),sum(num))  
   


# --------------------------------------------------
if __name__ == '__main__':
    main()
