#!/usr/bin/env python2.7

import argparse
import itertools

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
    return a.parse_args()

def lists_equal_to_length_of_shortest(list_a,list_b):
    """
    :param list_a, list_b:
    :return: Boolean
    """
    stripped_a = [a for a in list_a if a != '']
    stripped_b = [b for b in list_b if b != '']
    zipped = itertools.izip(stripped_a, stripped_b)
    equal = True
    for z in zipped:
        if z[0] != z[1]:
            equal = False
    return equal

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
        append_this_line = True
        for split_path in split_paths:
            if lists_equal_to_length_of_shortest(line, split_path):
                append_this_line = False
        if append_this_line:
            split_paths.append(line)
    paths = ['/'.join(split_path) for split_path in split_paths]
    return paths

def main(in_file, out_file=None):
    with open(in_file, 'r') as in_f:
        lines = [l.strip() for l in in_f.readlines()]

    to_write = process_paths(lines)
    if out_file:
        with open(out_file, 'w') as out_f:
            for out_line in to_write:
                out_f.write(out_line + '\n')
    else:
        for out_line in to_write:
            print(out_line)
if __name__ == "__main__":
    args = get_args()
    main(args.in_file, args.out_file)
