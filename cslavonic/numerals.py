# coding: utf-8
'''
Created on Feb 25, 2016

Support for Cyrillic Numerals
See UTN 41 for implementation information
http://www.unicode.org/notes/tn41/

Code was based on C++ OpenOffice code by Aleksandr Andreev: https://gerrit.libreoffice.org/#/c/20013/
but eventually rewritten to better match the desired behavior for large numbers 

@author: mike
'''
from __future__ import print_function, unicode_literals


CU_THOUSAND = '\u0482'
CU_TITLO    = '\u0483'
CU_TEN      = '\u0456'
CU_800      = '\u047f'
CU_NBSP     = '\u00a0'

CU_NUMBER_ARRAY = [
    ('\u0446', 900),
    ('\u047f', 800),
    ('\u0471', 700),
    ('\u0445', 600),
    ('\u0444', 500),
    ('\u0443', 400),
    ('\u0442', 300),
    ('\u0441', 200),
    ('\u0440', 100),
    ('\u0447',  90),
    ('\u043f',  80),
    ('\u047b',  70),
    ('\u046f',  60),
    ('\u043d',  50),
    ('\u043c',  40),
    ('\u043b',  30),
    ('\u043a',  20),
    ('\u0456',  10),
    ('\u0473',   9),
    ('\u0438',   8),
    ('\u0437',   7),
    ('\u0455',   6),
    ('\u0454',   5),
    ('\u0434',   4),
    ('\u0433',   3),
    ('\u0432',   2),
    ('\u0430',   1)
]
CU_NUMBER_DICT = dict(CU_NUMBER_ARRAY)
CU_DIGIT_DICT = dict((a,b) for b,a in CU_NUMBER_ARRAY)

def numeral_string(value, add_titlo=True, dialect='new'):
    
    if dialect not in ('old', 'new'):
        raise ValueError('unknown dialect "%s", expected one of: ["old", "new"]' % dialect)
    
    if value < 0:
        return '-' + numeral_string(-value, add_titlo=add_titlo)
    
    if value == 0:
        if add_titlo:
            return '0' + CU_TITLO
        else:
            return '0'
    
    groups = _make_groups_of_thousands(value)

    if len(groups) > 1:
        if len(groups[1]) == 1:
            # merge groups 0 and 1, because only single digit in groups[1]
            groups[1].extend(groups[0])
            del groups[0][:]  # groups[0].clear() - works only in Python 3
        elif len(groups[1]) > 1 and (len(groups[0]) == 0 or dialect == 'old'):
            # force thousand symbol before every digit in groups[1]
            groups[1] = _insert_thousand_before_each_digit(groups[1])
            if dialect == 'old':
                groups[1].extend(groups[0])
                del groups[0][:]  # groups[0].clear() - works only in Python 3

    if add_titlo:
        for group in groups:
            _insert_titlo(group)

    out = []
    while groups:
        group = groups.pop()
        if group:
            group = [CU_THOUSAND] * len(groups) + group
            out.append(''.join(group))

    return CU_NBSP.join(out)

def _insert_thousand_before_each_digit(group):
    return list(CU_THOUSAND.join(group))

def _make_small_number(value):
    ''' generates array of characters representing small Church Slavonic
        number. No titlo.'''
    assert 0 <= value < 1000, value
    
    out = []
    if value >= 100:
        z = (value // 100) * 100
        out.append(CU_DIGIT_DICT[z])
        value -= z
    
    if value > 10:
        if value < 20:
            out.extend(_make_small_number(value - 10))
            out.append(CU_TEN)
            value = 0
        else:
            z = (value // 10) * 10
            out.append(CU_DIGIT_DICT[z])
            value -= z
    
    if value > 0:
        out.extend(CU_DIGIT_DICT[value])

    return out


def _make_groups_of_thousands(value):
    '''returns groups of thousands as a list (in reverse order):
       Decimal  123456789 is split like this:
       123 456 789 then reversed to 789 456 123
       and finally each group is represented as Church Slavonic number:
       [ [789], [456], [123] ]
       reversal of order is just for technical convenience
    '''
    assert value > 0
    
    groups = []

    num = value
    while num > 0:
        groups.append(_make_small_number(num % 1000))
        num //= 1000

    return groups


def _insert_titlo(group):

    # need to filter out CU_THOUSAND marks when deciding on the titlo position
    digits = {}
    for i, x in enumerate(group):
        if x != CU_THOUSAND:
            digits[len(digits)] = i

    if len(digits) == 0:
        return

    elif len(digits) == 1 or group[digits[len(digits)-2]] == CU_800:
        group.append(CU_TITLO)

    else:
        group.insert(digits[len(digits)-2]+1, CU_TITLO)


def numeral_parse(string):
    s = string
    if string.startswith('-'):
        return -numeral_parse(string[1:])

    s = s.replace(CU_TITLO, '')
    
    if not s:
        raise ValueError('invalid number: ' + string)
    
    if s == '0':
        return 0
    
    groups = s.split()
    groupinfo = [(g, _multiplier(g)) for g in groups]

    # all multipliers must be different
    if len(set(x[1] for x in groupinfo)) != len(groupinfo):
        raise ValueError('invalid number: ' + string)
    
    # multipliers should be sorted reverse
    if sorted(groupinfo, key=lambda x: -x[1]) != groupinfo:
            raise ValueError('invalid number: ' + string)

    # special case: group with multiplier 1000 can be split (no group separators for numbers < 10000)
    multiplier = {b: a for a,b in groupinfo}
    if 1000 in multiplier:
        g1, g0 = _split_thousand(multiplier[1000])
        if 1 in multiplier:
            # just validate
            if len(g1) != 1:
                raise ValueError('invalid number: ' + string)
        elif g0:
            # yes, split was successful with non-empty group g0
            multiplier[1000] = g1
            multiplier[1] = g0

    # now we should remove thousands marks
    multiplier = {a: b.replace(CU_THOUSAND, '') for a,b in multiplier.items()}
    
    # and build total value from thousand groups
    value = sum(m*_parse_small_number(g) for m,g in multiplier.items())
    
    return value


def _multiplier(group):
    multiplier = 1
    for c in group:
        if c == CU_THOUSAND:
            multiplier *= 1000
        else:
            break
    return multiplier


def _split_thousand(group):
    assert group[0] == CU_THOUSAND
    assert group[1] != CU_THOUSAND

    # number of digits that have CU_THOUSAND prepended
    num = sum(1 for c in group if c == CU_THOUSAND)
    
    assert len(group) >= 2 * num
    assert min(group[i*2]==CU_THOUSAND for i in range(num)) == True
    
    group = group.replace(CU_THOUSAND, '')
    return group[:num], group[num:]


def _parse_small_number(val):
    
    if len(val) != len(set(val)):
        raise ValueError('invalid number: ' + val)

    value = 0
    for c in val:
        if c not in CU_NUMBER_DICT:
            raise ValueError('invalid number: ' + val)
        value += CU_NUMBER_DICT[c]
    
    return value

def _ensure_thousand_at_every_position(val):
    for i in range(len(val)):
        if i % 2 == 1:
            if val[i] != CU_THOUSAND:
                return False
        else:
            if val[i] == CU_THOUSAND:
                return False
    return True
    