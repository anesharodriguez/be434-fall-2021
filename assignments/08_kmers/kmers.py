#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-10-27
Purpose: Rock the Casbah
"""

import argparse
import io
from collections import defaultdict


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
                        help='Kmer size',
                        metavar='INT',
                        type=int,
                        default=3)

    args = parser.parse_args()
    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    kmers1 = count_kmers(args.file1, args.kmer)
    kmers2 = count_kmers(args.file2, args.kmer)

    for common in set(kmers1).intersection(set(kmers2)):
        print('{:10} {:5} {:5}' .format(
            common, kmers1.get(common), kmers2.get(common)))
# -------------------------------------------------
def count_kmers(fh, k):

    kmers = defaultdict(int)

    for line in fh:
        for word in line.split():
            for kmer in find_kmers(word, k):
                kmers[kmer] += 1
    return kmers
# ---------------------------------------------------
def test_count_kmers():
    """ Test count_kmers """
    dat = 'foo\nbar\nbaz\n'
    assert count_kmers(io.StringIO(dat), 3) == {'foo': 1, 'bar': 1, 'baz': 1}
    assert count_kmers(io.StringIO(dat), 2) == {
        'fo': 1,
        'oo': 1,
        'ba': 2,
        'ar': 1,
        'az': 1
    }
# ----------------------------------------------------
def find_kmers(word, k):
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
