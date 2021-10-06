#!/usr/bin/env python3
"""
Author : anesharodriguez <anesharodriguez@localhost>
Date   : 2021-10-05
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    codon_table = {}
    for line in args.codons:
        key, val = line.rstrip().split()
        codon_table[key] = val

    protein = ''
    k = 3
    seq = args.sequence.upper()
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        # print(codon)
        protein += codon_table.get(codon, '-')

    print(protein, file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')

    # pprint(codon_table)
    # print('seq =', args.sequence)
    # print('codons =', args.codons)
    # print('outfile =', args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
