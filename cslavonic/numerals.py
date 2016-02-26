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
    return ''.join(_make_number(value, add_titlo=add_titlo))


def _make_number(value, *, add_titlo=True):
    out = []
    
    num = value % 1000
    
    if value >= 1000:
        out.append(CU_THOUSAND)
        out.extend(_make_number(value // 1000, add_titlo=False))
        
        if value >= 10000 and ((value - 10000) % 1000) != 0:
            out.append(' ')

        if value % 1000 == 0:
            add_titlo = False

    for c,x in CyrillicNumberCharArray:
        if num <= 0:
            break
        
        if 10 < num < 20:
            num -= 10
            out.extend(_make_number(num, add_titlo=False))
            out.append(CU_TEN)
            break

        if x <= num:
            out.append(c)
            num -= x

    if add_titlo:
        if len(out) == 1:
            out.append(CU_TITLO)
        elif len(out) >= 2:
            if len(out) > 2 and out[-2] ==' ':
                out.append(CU_TITLO)
            elif 800 < (value % 1000) < 9000:
                out.append(CU_TITLO)
            else:
                out.insert(len(out)-1, CU_TITLO)
    
    return out
