#!/usr/local/bin/python3
'''
Created on Feb 4, 2016

@author: mike
'''
from __future__ import print_function, unicode_literals
import argparse
import codecs
from cslavonic import ucs_codec
import sys


def main_reencode(args):
    
    ucs_codec.register_UCS()
    
    with codecs.open(args.input or sys.stdin.fileno(), 'r', args.encoding) as src:
        with codecs.open(args.output or sys.stdout.fileno(), 'w', 'utf-8') as dest:
            dest.write(src.read())

    return 0


def main():
    parser = argparse.ArgumentParser(description='Converts file from UCS (or any other input encoding) to utf-8')
    parser.add_argument('-i', '--input', default=None, help='File to decode. If not set, reads STDIN')
    parser.add_argument('-e', '--encoding', default='UCS', help='Input file encoding. Default is UCS')
    parser.add_argument('-o', '--output', default=None, help='File to create. If not set, writes to STDOUT.')
    
    args = parser.parse_args()
    
    parser.exit(main_reencode(args))


if __name__ == '__main__':
    main()