'''
Created on Feb 25, 2016

Support for Cyrillic Numerals
See UTN 41 for implementation information
http://www.unicode.org/notes/tn41/

Code was based on C++ OpenOffice code by Aleksandr Andreev: https://gerrit.libreoffice.org/#/c/20013/
but eventually rewritten to better matched desired behavior on large numbers 

@author: mike
'''
import re

CU_THOUSAND = '\u0482'
CU_TITLO    = '\u0483'
CU_TEN      = '\u0456'
CU_800      = '\u047f'

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

def numeral_string(value, *, add_titlo=True):
    
    if value < 0:
        return '-' + numeral_string(-value, add_titlo=add_titlo)
    
    if value == 0:
        if add_titlo:
            return '0' + CU_TITLO
        else:
            return '0'
    
    groups = _make_groups_of_thousands(value)

    if value < 10000:
        group = groups[0]
        if value >= 1000:
            group = groups[1] + groups[0]
        if add_titlo:
            _insert_titlo(group)
        if value >= 1000:
            group.insert(0, CU_THOUSAND)
        return ''.join(group)
    
    if add_titlo:
        for group in groups:
            _insert_titlo(group)
    
    if not groups[0]:  # same as if (value % 1000) == 0
        # potential ambiguity - lets insert CU_THOUSAND before each digit in groups[1]
        _insert_thousand_before_each_numeral(groups[1])
    
    out = []
    while groups:
        group = groups.pop()
        if group:
            group = [CU_THOUSAND] * len(groups) + group
            out.append(''.join(group))
    
    return ' '.join(out)

def _insert_thousand_before_each_numeral(group):
    for i in reversed(range(1, len(group))):
        if group[i] != CU_TITLO:
            group.insert(i, CU_THOUSAND)
    
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

    if len(group) == 0:
        return

    elif len(group) == 1 or group[-2] == CU_800:
        group.append(CU_TITLO)

    else:
        group.insert(-1, CU_TITLO)


def numeral_parse(string):
    minus = False
    
    s = string
    if string.startswith('-'):
        minus = True
        s = s[1:]
    
    s = re.sub(CU_TITLO, '', s)
    
    if not s:
        raise ValueError('invalid number: ' + string)
    
    if s == '0':
        return 0
    
    groups = s.split()
    if len(groups) == 1:
        val = groups[0]

        multiplier = 1
        mtc = re.match('(' + CU_THOUSAND + r'{1,})', val)
        if mtc:
            multiplier = 1000 ** len(mtc.group(1))
        
        if multiplier == 1:
            value = _parse_small_number(val)
        
        elif multiplier == 1000:
            # number between 1000 and 10000
            val = val[1:]
            
            if CU_THOUSAND in val:
                # have more marks
                # then marks must be on every odd position
                if not _ensure_thousand_at_every_position(val):
                    raise ValueError('invalid number: ' + string)
                val = re.sub(CU_THOUSAND, '', val)
                
                value = _parse_small_number(val) * 1000
            else:
                value = _parse_small_number(val[0]) * 1000 + _parse_small_number(val[1:])
        else:
            val = val[mtc.end():]
            value = multiplier * _parse_small_number(val)
    else:
        # easy case, make sure we have desired number of thousand marks at every position
        multiplier = [1] * len(groups)
        for i in range(len(groups)):
            mtc = re.match('(' + CU_THOUSAND + r'*)', groups[i])
            if not mtc:
                raise ValueError('invalid number: ' + string)
            multiplier[i] = 1000**len(mtc.group(1))
            groups[i] = groups[i][mtc.end():]
            
            if len(mtc.group(1)) == 1:
                if CU_THOUSAND in groups[i]:
                    if not _ensure_thousand_at_every_position(groups[i]):
                        raise ValueError('invalid number: ' + string)
                    groups[i] = re.sub(CU_THOUSAND, '', groups[i])
        
        if len(set(multiplier)) != len(multiplier):
            raise ValueError('invalid number: ' + string)
        if sorted(multiplier, reverse=True) != multiplier:
            raise ValueError('invalid number: ' + string)
        
        value = 0
        for m,g in zip(multiplier, groups):
            value += m * _parse_small_number(g)
        
    return -value if minus else value

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
    