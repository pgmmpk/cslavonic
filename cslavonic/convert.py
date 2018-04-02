# coding: utf-8
from __future__ import print_function, unicode_literals

import re
import os
import collections
from cslavonic.numerals import CU_TITLO, CU_THOUSAND


CU_DIGIT_LETTER = '[авгдєѕзиѳіклмнѯопчрстуфхѱѿц]'
MAYBE_DIGIT_REGEX = re.compile(
    r'\b' + CU_THOUSAND + '{0,2}' + CU_DIGIT_LETTER + '+' + CU_TITLO + CU_DIGIT_LETTER + r'*\b',
    re.IGNORECASE+re.UNICODE)

def _replace_digits(text):
    def sub(mtc):
        try:
            return cu_parse_int(mtc.group())
        except ValueError:
            return mtc.group()  # no changes

    return re.sub(MAYBE_DIGIT_REGEX, sub, text)

def expand_titlo(text):
    text = _replace_titlo(text)
    text = _replace_digits(text)
    return text

def _build_replacer(mapping):

    regexp = re.compile('|'.join(x.replace('.', r'\b') for x in mapping.keys()), flags=re.MULTILINE+re.UNICODE)
    values = {x.replace(r'\b', ''): y for x, y in mapping.items()}

    for k in mapping.keys():
        if k.startswith('\\bбг'):
            print(k)

    def replacer(text):
        return re.sub(regexp, lambda mtc: values[mtc.group()], text)

    return replacer

def _res(*av):
    return os.path.join(os.path.dirname(__file__), 'resources', *av)

def _read_untitlo_map():
    with open(_res('untitlo.tsv'), 'rb') as f:
        for line in f:
            line = line.decode('utf-8')
            line = line.strip()
            if not line or line[0] == '#':
                continue
            parts = line.split('\t')
            assert len(parts) == 2, parts
            key = parts[0].replace('.', r'\b')
            yield key, parts[1]

_replace_titlo = _build_replacer(collections.OrderedDict(_read_untitlo_map()))
