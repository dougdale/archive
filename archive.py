#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
archive.py

A script to recursively archive files older than a certain amount by moving
them from one directory to another.
"""

import sys
import argparse


def main(arguments):
    """Set up arguments, call body, handle errors"""

    formatter_class = argparse.ArgumentDefaultsHelpFormatter
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=formatter_class)

    parser.add_argument('--years', help="Archive files older than X years",
                        default=2)

    # TODO Add --date option

    parser.add_argument('source', help="Source directory")
    parser.add_argument('destination', help="Destination directory")

    args = parser.parse_args(arguments)
    print(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
