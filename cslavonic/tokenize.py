# coding: utf-8
from __future__ import print_function, unicode_literals

import re
from cslavonic.numerals import CU_THOUSAND


CU_LETTERS_LOWER = 'абвгдеєжѕзꙁиіїйклмноѻпрстуꙋфхѡѿѽꙍцчшщъыьѣюѧѫꙗѯѱѳѵѷ'
CU_LETTERS_UPPER = 'АБВГДЕЄЖЅЗꙀИІЇЙКЛМНОѺПРСТУꙊФХѠѾѼꙌЦЧШЩЪЫЬѢЮѦѪꙖѮѰѲѴѶ\u1c82\u1c81'
CU_COMBINING_ACCENTS = '\u0483-\u0489'
CU_SMALL_COMBINING_LETTERS = '\u2de0-\u2dff'
RU_EXTRAS = 'ЭяэЙёЯЁй'  # Russian letters not in CU_LETTERS
CU_EXTRAS = 'ЀЁЃЇЌЍЎЙйѐёѓїќѝўѶѷ'  # un-normalized forms
ENG_LETTERS = 'a-zA-Z'
DIACRITICAL = '\u0300-\u036f'
GREEK_LETTERS = '\u0370-\u03ff'

CU_W_REGEX = re.compile('[' +
    CU_LETTERS_LOWER +
    CU_LETTERS_UPPER +
    RU_EXTRAS +
    CU_EXTRAS +
    ENG_LETTERS +
    GREEK_LETTERS +
    CU_THOUSAND +
    CU_COMBINING_ACCENTS +
    CU_SMALL_COMBINING_LETTERS +
    DIACRITICAL +
']+', flags=re.MULTILINE + re.UNICODE)

NUMBER_REGEX = re.compile('(\d+(,\d\d\d){0,2})(\.\d+)?', re.MULTILINE + re.UNICODE)

def tokenize(text):
    '''
    Text tokenizer. Suitable for use with CU, civil CU, and RU.

    Rules:
        - sequence of whitespace characters is a single token
        - sequence of Russian, Church-slavonic, or English letters is a single token
        - civil number is a single token (allows decimals and thousands)
        - everything else is treated as punctuation and split one character per token
    '''
    offset = 0
    for mtc in re.finditer(CU_W_REGEX, text):
        s, e = mtc.start(), mtc.end()
        for tk in _tokenize_nonletters(text[offset:s]):
            yield tk
        yield text[s:e]
        offset = e
    for tk in _tokenize_nonletters(text[offset:]):
        yield tk

def _tokenize_nonletters(text):
    offset = 0
    for mtc in re.finditer(r'\s+', text, flags=re.MULTILINE+re.UNICODE):
        s, e = mtc.start(), mtc.end()
        if offset < s:
            for tk in _tokenize_numbers(text[offset:s]):
                yield tk
        yield text[s:e]
        offset = e
    if offset < len(text):
        for tk in _tokenize_numbers(text[offset:]):
            yield tk

def _tokenize_numbers(text):
    offset = 0
    for mtc in re.finditer(NUMBER_REGEX, text):
        s, e = mtc.start(), mtc.end()
        for i in range(offset, s):
            yield text[i]
        yield text[s:e]
        offset = e
    for i in range(offset, len(text)):
        yield text[i]
