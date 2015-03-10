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
    return a.parse_args

def process_paths(lines_from_file):
    paths = []
    split_paths = []

    # Split up lines and sort by the length of the path, largest first:
    split_lines = [l.split('/') for l in lines_from_file]
    lines_by_path_length = sorted(split_lines, key=len, reverse=True)

    # Append the longest path to split paths, then see if the others are
    # subsets of it.
    try:
        split_paths.append(lines_by_path_length[0])
    except IndexError:
        raise Exception('No paths in input file ')

    for line in lines_by_path_length:
        for path in paths:
            pass


    return paths

def main(in_file, out_file):
    with open(in_file, 'r') as in_f:
        lines = [l.strip() for l in in_f.readlines()]
    with open(out_file, 'w') as out_f:
        for out_line in process_paths(lines):
            out_f.write(out_line)

if __name__ == "__main__":
    args = get_args()
    main(args.in_file, args.out_file)
