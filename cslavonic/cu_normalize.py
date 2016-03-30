# coding: utf-8
'''
Created on Feb 16, 2016

@author: mike
'''
import argparse
import codecs
import re
import sys
from cslavonic.normalize import explode_nfd


def main_explain(args):
    print(
'''
Church Slavonic letter "uk" is a digraph, composed of letters "sharp o" and "u". 
Unicode standard (version 8.0.0) suggests that letter "uk" is represented by a 
ligature glyph U+0479.

However, there is a pending request to deprecate this codepoint and represent the 
same digraph with a pair of U+1C82 U+0443, see

    http://www.unicode.org/notes/tn41/tn41-1.pdf

There are good reasons for that and it is expected that request will be approved 
and future versions of Unicode standard will recommend using two codepoints for
the "uk" digraph. 

This utility allows one to re-encode text document both ways:

   ligature - make sure that two-letter sequences of U+1C82 U+0443 are replaced 
              with the ligature (compatibility mode, works with fonts and software
              that implements current Unicode standard).
   unligature - replace ligatures with two-letter sequence (bleeding-edge mode, 
              expected to be recommended by future edition of Unicode. Not all 
              fonts and software support this yet).
   hyph - processes TeX hyphenation patterns to make sure that all possible combina tions
              of NFC and NFD character forms are covered by pattern and exception.
''')
    return 0


def main_ligature(args):

    with codecs.open(args.input or sys.stdin.fileno(), 'r', 'utf-8') as f:
        with codecs.open(args.output or sys.stdout.fileno(), 'w', 'utf-8') as out:
            out.write(re.sub('\u1c82\u0443', '\u0479', f.read()))

    return 0


def main_unligature(args):

    with codecs.open(args.input or sys.stdin.fileno(), 'r', 'utf-8') as f:
        with codecs.open(args.output or sys.stdout.fileno(), 'w', 'utf-8') as out:
            out.write(re.sub('\u0479', '\u1c82\u0443', f.read()))

    return 0


def main_hyph(args):

    with codecs.open(args.input or sys.stdin.fileno(), 'r', 'utf-8') as f:
        with codecs.open(args.output or sys.stdout.fileno(), 'w', 'utf-8') as out:
            
            for line in f:
                for l in explode_nfd(line):
                    out.write(l)

    return 0


def main():
    parser = argparse.ArgumentParser(description='Utilities to deal with "uk" letter in its expanded or ligature form. Use "explain" command to get more information.')
    sub = parser.add_subparsers(help='Command', dest='cmd')
    
    parser_explain = sub.add_parser('explain', help='Prints explanation')  # @UnusedVariable
    
    parser_ligature = sub.add_parser('ligature', help='Collapse all "sharp o"+"u" sequences into a single "uk" ligature symbol')
    parser_ligature.add_argument('input', help='Input file')
    parser_ligature.add_argument('output', help='Output file')
    
    parser_unligature = sub.add_parser('unligature', help='Expand all "uk" ligatures into a combination of "sharp o" and "u" characters')
    parser_unligature.add_argument('input', help='Input file')
    parser_unligature.add_argument('output', help='Output file')
    
    parser_hyph = sub.add_parser('hyph', help='Makes TeX hyphenation patterns file compatible with inputs that use expanded or collapsed version of "uk" by repeating each pattern that contains "uk" in ech variant')
    parser_hyph.add_argument('input', help='Input file')
    parser_hyph.add_argument('output', help='Output file')
    
    args = parser.parse_args()
    
    if args.cmd == 'explain':
        parser.exit(main_explain(args))
    elif args.cmd == 'ligature':
        parser.exit(main_ligature(args))
    elif args.cmd == 'unligature':
        parser.exit(main_unligature(args))
    elif args.cmd == 'hyph':
        parser.exit(main_hyph(args))
    else:
        parser.error('Missing or invalid command')
        

if __name__ == '__main__':
    main()