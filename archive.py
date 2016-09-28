#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
archive.py

A script to recursively archive files older than a certain amount by moving
them from one directory to another.
"""

import sys
import argparse
import os
import re

def main(args):
    """Main routine when run from command line"""

    skipdirs = re.compile(r'\.[^\.\\/]+')

    for directory, subdirs, files in os.walk(args.source):
        if not skipdirs.match(directory):
            print('Directory:', directory)
            for file in files:
                print('\t', file)

if __name__ == '__main__':
    formatter_class = argparse.ArgumentDefaultsHelpFormatter

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=formatter_class)

    parser.add_argument('--years', help="Archive files older than X years",
                        default=2)

    # TODO Add --date option

    parser.add_argument('source', help="Source directory")
    parser.add_argument('destination', help="Destination directory")

    args = parser.parse_args(sys.argv[1:])
    print(args)

    sys.exit(main(args))
