# coding: utf-8
'''
Created on Feb 25, 2016

Support for Cyrillic Numerals
See UTN 41 for implementation information
http://www.unicode.org/notes/tn41/

Code was based on C++ OpenOffice code by Aleksandr Andreev: https://gerrit.libreoffice.org/#/c/20013/
but eventually rewritten to implement more features. 

@author: mike
'''
from __future__ import print_function, unicode_literals


CU_THOUSAND = '\u0482'
CU_TITLO    = '\u0483'
CU_800      = '\u047f'
CU_NBSP     = '\u00a0'

CU_NUMBER = {
    '\u0446': 900,
    '\u047f': 800,
    '\u0471': 700,
    '\u0445': 600,
    '\u0444': 500,
    '\u0443': 400,
    '\u0442': 300,
    '\u0441': 200,
    '\u0440': 100,
    '\u0447':  90,
    '\u043f':  80,
    '\u047b':  70,
    '\u046f':  60,
    '\u043d':  50,
    '\u043c':  40,
    '\u043b':  30,
    '\u043a':  20,
    '\u0456':  10,
    '\u0473':   9,
    '\u0438':   8,
    '\u0437':   7,
    '\u0455':   6,
    '\u0454':   5,
    '\u0434':   4,
    '\u0433':   3,
    '\u0432':   2,
    '\u0430':   1,
}

CU_DIGIT = {b: a for a, b in CU_NUMBER.items()}


def cu_format_int(value, add_titlo=True, dialect='standard'):
    '''
    Formats an integer :value: as Church Slavonic number (string).
    
    Parameters:
        :value: - the value to format (an int).
        :add_titlo: - if True (default), adds titlo.
        :dialect: - controls how large numbers are generated. Default is "standard".
    '''
    
    if dialect not in ('old', 'standard'):
        raise ValueError('unknown dialect "%s", expected one of: ["old", "standard"]' % dialect)
    
    if value < 0:
        return '-' + cu_format_int(-value, add_titlo=add_titlo)
    
    if value == 0:
        if add_titlo:
            return '0' + CU_TITLO
        else:
            return '0'
    
    groups = _format_thousand_groups(value)

    if len(groups) > 1:
        if len(groups[-2]) == 1:
            # merge groups -1 and -2, because only a single digit in groups[-2]
            groups[-2] = groups[-2] + groups[-1]
            groups[-1] = ''
        elif len(groups[-2]) > 1 and (len(groups[-1]) == 0 or dialect == 'old'):
            # force thousand symbol before every digit in groups[1]
            groups[-2] = _insert_thousand_before_each_digit(groups[-2])
            if dialect == 'old':
                groups[-2] = groups[-2] + groups[-1]
                groups[-1] = ''

    if add_titlo:
        groups = [_place_titlo(x) for x in groups]

    # add leading thousand signs. Last group gets none, last but one gets one, etc
    out = [ CU_THOUSAND * (len(groups)-1-i) + group for i,group in enumerate(groups) if group]

    return CU_NBSP.join(out)

def _format_small_number(value):
    '''
    Deals with numbers in the range 0...999 inclusively
    '''
    assert 0 <= value < 1000, value

    hundreds = (value // 100) * 100
    value -= hundreds
    tens     = (value // 10) * 10
    value -= tens
    
    out = []
    if hundreds:
        out.append(CU_DIGIT[hundreds])
    
    if tens == 10:
        # numbers between 11..19 (inclusive) use reverse order of digits due
        # to pronunciation rules (digit order in Church Slavonic follows pronunciation)
        if value:
            out.append(CU_DIGIT[value])
        out.append(CU_DIGIT[tens])
    else:
        if tens:
            out.append(CU_DIGIT[tens])
        if value:
            out.append(CU_DIGIT[value])

    return ''.join(out)


def _format_thousand_groups(value):
    '''
    Returns groups of thousands as a list:
    
    Decimal  123456789 is split like this:
    123 456 789 and each group is formatted as a Church Slavonic number string:
    [ '123', '456', '783' ] (where strings are actually using Church Slavonic digits)
    '''
    assert value >= 0
    
    groups = []
    while value > 0:
        groups.append(_format_small_number(value % 1000))
        value //= 1000

    return list(reversed(groups))


def _insert_thousand_before_each_digit(group):
    return CU_THOUSAND.join(group)


def _place_titlo(numstring):
    if not numstring:
        return numstring

    if len(numstring) > 1:
        if numstring[-2] != CU_THOUSAND:
            if numstring[-2] != CU_800:
                return numstring[:-1] + CU_TITLO + numstring[-1:]
        else:
            if len(numstring) > 2:
                if numstring[-3] != CU_THOUSAND:  # e.g. not "##a"
                    if numstring[-3] != CU_800:
                        return numstring[:-2] + CU_TITLO + numstring[-2:]
    return numstring + CU_TITLO


def cu_parse_int(string):
    '''
    Parses Church Slavonic number string. Input string can use any dialect - parser will
    detect and handle accordingly.
    '''
    s = string
    if string.startswith('-'):
        return -cu_parse_int(string[1:])

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
        if c not in CU_NUMBER:
            raise ValueError('invalid number: ' + val)
        value += CU_NUMBER[c]
    
    return value
