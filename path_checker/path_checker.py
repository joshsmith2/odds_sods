#!/usr/bin/env python3

import argparse

def get_args():
    a = argparse.ArgumentParser(description="From a file containing a bunch of"
                                            " paths, write out a file which"
                                            " only contains child and no"
                                            "parent directories. (E.g /usr/ but"
                                            "not /usr/bin.")
    a.add_argument('-i', '--in-file', metavar='PATH', dest='in_file',
                   help='File containing paths')
    a.add_argument('-o', '--out-file', metavar='PATH', dest='out_file',
                   help='File to write out to. Else print to stdout.')
    return p.parse_args

def process_paths(lines_from_file):
    paths = []
    for line in lines_from_file:



def main(in_file, out_file):
    with open(in_file, 'r') as f:
        unstripped = f.readlines()
        lines = [ l.strip() for l in unstripped ]


if __name__ == "__main__":
    args = get_args()
    main(args.in_file, args.out_file)
