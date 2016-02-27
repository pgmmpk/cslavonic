'''
Created on Feb 25, 2016

Support for Cyrillic Numerals
See UTN 41 for implementation information
http://www.unicode.org/notes/tn41/

This is a direct port of C++ OpenOffice code by Alexander Andreev: https://gerrit.libreoffice.org/#/c/20013/

@author: mike
'''

CU_THOUSAND = '\u0482'
CU_TITLO    = '\u0483'
CU_TEN      = '\u0456'
CU_800      = '\u047f'

CyrillicNumberCharArray = [
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
    
    if not groups[0]:
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
    for c,x in CyrillicNumberCharArray:
        if value <= 0:
            break
        
        if 10 < value < 20:
            out.extend(_make_small_number(value - 10))
            out.append(CU_TEN)
            break

        if x <= value:
            out.append(c)
            value -= x
    
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

