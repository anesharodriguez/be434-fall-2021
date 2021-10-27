#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-10-27
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = {}
    file2 = {}
    total_kmers =0
    k=0
    for line in args.file1:
        kmers_word = 0
        for word in line.split():
            file1[word] = 1
     
    for line in args.file2:
        for word in line.split():
            file2[word] = 1

    for word in file1:
            if word in file2:
                for kmer in find_kmers(word,k):
    
                    kmers_word += len(line.split())
           
                total_kmers += kmers_word
    
                print(word,total_kmers)
# ----------------------------------------------------
def find_kmers(word,k):
    """Find k-mers in string"""
    n = len(word) - k + 1
    return [] if n < 1 else [word[i:i + k] for i in range(n)]
# -----------------------------------------------------
def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []
# --------------------------------------------------
if __name__ == '__main__':
    main()
