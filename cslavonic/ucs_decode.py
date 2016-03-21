'''
Created on Feb 4, 2016

Decoding tables taken from https://github.com/typiconman/Perl-Lingua-CU

@author: mike kroutikov
'''
from __future__ import print_function, unicode_literals
import codecs


def ucs_decode(input_, errors='strict'):
    return ''.join(decoding_table[x] for x in input_), len(input_)


def ucs_encode(input_, errors):
    raise NotImplementedError('encoding to UCS is not implemented')


### Decoding Table
decoding_table = (
    '\x00',
    '\x01',
    '\x02',
    '\x03',
    '\x04',
    '\x05',
    '\x06',
    '\x07',
    '\x08',
    '\t',
    '\n',
    '\x0b',
    '\x0c',
    '\r',
    '\x0e',
    '\x0f',
    '\x10',
    '\x11',
    '\x12',
    '\x13',
    '\x14',
    '\x15',
    '\x16',
    '\x17',
    '\x18',
    '\x19',
    '\x1a',
    '\x1b',
    '\x1c',
    '\x1d',
    '\x1e',
    '\x1f',
    ' ',
    '!',
    '"',
    '\u0486',
    '\u0486\u0301',
    '\u0486\u0300',
    '\u0483',
    "'",
    '(',
    ')',
    '\ua673',
    '\u2de1\u0487',  # combining VE
    ',',
    '-',
    '.',
    '/',
    '\u043e\u0301',
    '\u0301',
    '\u0300',
    '\u0486',
    '\u0486\u0301',
    '\u0486\u0300',
    '\u0311',  # combining inverted breve
    '\u0483',  # titlo
    '\u033e',  # combining vertical tilde
    '\u0436\u0483',  # zhe with titlo above
    ':',
    ';',
    '\u2def',  # combining HA
    '\u2de9\u0487',  # combining EN
    '\u2dec\u0487',  # combining ER
    '\u2df1\u0487',  # combining CHE
    '\u0300',
    '\u0430\u0300',  # latin A maps to AZ with grave accent
    '\u0463\u0311',  # latin B maps to Yat' with inverted breve
    '\u2ded\u0487',  # combining ES
    '\u0434\u2ded\u0487',
    '\u0435\u0300',  # latin E maps to e with grave accent
    '\u0472',  # F maps to THETA
    '\u0433\u0483',  # G maps to ge with TITLO
    '\u0461\u0301',  # latin H maps to omega with acute accent
    '\u0406',
    '\u0456\u0300',
    '\ua656\u0486',  # YA with psili
    '\u043b\u2de3',  # el with cobining de
    '\u0476',  # capital IZHITSA with kendema
    '\u047a\u0486',  # capital WIDE ON with psili
    '\u047a',  # just capital WIDE ON
    '\u0470',  # capital PSI
    '\u047c',  # capital omega with great apostrophe
    '\u0440\u0483',  # lowercase re with titlo
    '\u0467\u0300',  # lowercase small yus with grave
    '\u047e',  # capital OT
    '\u041e\u0443',  # diagraph capital UK
    '\u0474',  # capital IZHITSA
    '\u0460',  # capital OMEGA
    '\u046e',  # capital XI
    '\ua64b\u0300',  # monograph uk with grave
    '\u0466',  # capital SMALL YUS
    '[',
    '\u0483',  # yet another titlo
    ']',
    '\u0311',  # combining inverted breve
    '\u033e',  # yet another yerik
    '`',
    '\u0430\u0301',  # latin A maps to AZ with acute accent
    '\u2dea\u0487',  # combining ON
    '\u2ded\u0487',  # combining ES
    '\u2de3',  # combining DE
    '\u0435\u0301',  # latin E maps to e with acute accent
    '\u0473',  # lowercase theta
    '\u2de2\u0487',  # combining ge
    '\u044b\u0301',  # ery with acute accent
    '\u0456',
    '\u0456\u0301',  # i with acute accent
    '\ua657\u0486',  # iotaed a with psili
    '\u043b\u0483',  # el with titlo
    '\u0477',  # izhitsa with izhe titlo
    '\u047b\u0486',  # wide on with psili
    '\u047b',  # wide on
    '\u0471',  # lowercase psi
    '\u047d',  # lowercase omega with great apostrophe
    '\u0440\u2ded\u0487',  # lowercase er with combining es
    '\u0467\u0301',  # lowercase small yus with acute accent
    '\u047f',  # lowercase ot
    '\u1c82\u0443',  # diagraph uk
    '\u0475',  # lowercase izhitsa
    '\u0461',  # lowercase omega
    '\u046f',  # lowercase xi
    '\ua64b\u0301',  # monograph uk with acute accent
    '\u0467',  # lowercase small yus
    '\ua64b\u0311',  # monograph uk with inverted breve
    '\u0467\u0486\u0300',  # lowercase small yus with apostroph
    '\u0438\u0483',  # the numeral eight
    '\u0301',  # yet another acute accent
    '\x7f',
    '\u0475\u0301',  # lowercase izhitsa with acute
    '\u0410\u0486\u0301',  # uppercase A with psili and acute
    '\u201a',
    '\u0430\u0486\u0301',  # lowercase A with psili and acute
    '\u201e',
    '\u046f\u0483',  # the numberal sixty
    '\u0430\u0311',  # lowercase a with inverted breve
    '\u0456\u0311',  # lowercase i with inverted breve
    '\u2de5',  # combining ze
    '\u0467\u0311',  # lowercase small yus with inverted breve
    '\u0466\u0486',  # upercase small yus with psili
    '\u0456\u0483',  # the numeral ten
    '\u0460\u0486',  # capital OMEGA with psili
    '\u041e\u0443\u0486\u0301',  # diagraph uk with apostroph
    '\ua656\u0486\u0301',  # uppercase Iotated A with apostroph
    '\u047a\u0486\u0301',  # uppercase Round O with apostroph
    '\u0475\u2de2\u0487',  # lowercase izhitsa with combining ge
    '\u2018',
    '\u2019',
    '\u201c',
    '\u201d',
    '\u2de4',  # combining zhe
    '\u2013',
    '\u2014',
    '\ufffe',
    '\u0442\u0483',
    '\u0467\u0486',  # lowercase small yus with psili
    '\u0475\u0311',  # izhitsa with inverted breve
    '\u0461\u0486',  # lowercase omega with psili
    '\u1c82\u0443\u0486\u0301',  # diagraph uk with apostroph
    '\ua657\u0486\u0301',  # lowercase iotaed a with apostroph
    '\u047b\u0486\u0301',  # lowercase Round O with apostroph
    '\xa0',
    '\u041e\u0443\u0486',  # Capital Diagraph Uk with psili
    '\u1c82\u0443\u0486',  # lowercase of the above
    '\u0406\u0486\u0301',  # Uppercase I with apostroph
    '\u0482',  # cyrillic thousands sign
    '\u0410\u0486',  # capital A with psili
    '\u0445\u0483',  # lowercase kha with titlo
    '\u0447\u0483',  # the numeral ninety
    '\u0463\u0300',  # lowecase yat with grave accent
    '\u0441\u0483',  # the numeral two hundred
    '\u0404',
    '\xab',
    '\xac',
    '\xad',
    '\u0440\u2de3',  # lowercase er with dobro titlo
    '\u0406\u0486',
    '\ua67e',  # kavyka
    '\ua657\u0486\u0300',
    '\u0406',
    '\u0456\u0308',
    '\u0430\u0486',
    '\u0443',  # small letter u (why encoded at the micro sign?!)
    '\xb6',
    '\xb7',
    '\u0463\u0301',  # lowercase yat with acute accent
    '\u0430\u0483',  # the numeral one
    '\u0454',  # wide E
    '\xbb',
    '\u0456\u0486\u0301',  # lowercase i with apostroph
    '\u0405',
    '\u0455',
    '\u0456\u0486',  # lowercase i with psili
    '\u0410',
    '\u0411',
    '\u0412',
    '\u0413',
    '\u0414',
    '\u0415',
    '\u0416',
    '\u0417',
    '\u0418',
    '\u0419',
    '\u041a',
    '\u041b',
    '\u041c',
    '\u041d',
    '\u041e',
    '\u041f',
    '\u0420',
    '\u0421',
    '\u0422',
    '\ua64a',
    '\u0424',
    '\u0425',
    '\u0426',
    '\u0427',
    '\u0428',
    '\u0429',
    '\u042a',
    '\u042b',
    '\u042c',
    '\u0462',  # capital yat
    '\u042e',
    '\ua656',  # capital Iotified A
    '\u0430',
    '\u0431',
    '\u0432',
    '\u0433',
    '\u0434',
    '\u0435',
    '\u0436',
    '\u0437',
    '\u0438',
    '\u0439',
    '\u043a',
    '\u043b',
    '\u043c',
    '\u043d',
    '\u043e',
    '\u043f',
    '\u0440',
    '\u0441',
    '\u0442',
    '\ua64b',  # monograph Uk (why?!)
    '\u0444',
    '\u0445',
    '\u0446',
    '\u0447',
    '\u0448',
    '\u0449',
    '\u044a',
    '\u044b',
    '\u044c',
    '\u0463',  # lowercase yat
    '\u044e',
    '\ua657',  # iotaed a
)


def _build_decoding_table(fname):
    '''unitily to build decoding_table from Perl's ucsequivs file. we base on cp1251 and overlay data from ucsequivs'''
    from encodings import cp1251

    decode_table = list(cp1251.decoding_table)
    comments = [None] * 256
    
    with codecs.open(fname, 'r', 'utf-8') as f:
        
        for line in f:
            line = line.strip()
            if not line or line == 'use utf8;' or line.startswith('#'):
                continue

            key, chars, comment = parse_perl_dictionary_entry(line)

            decode_table[key] = chars
            comments[key] = comment

    return decode_table, comments


def parse_perl_dictionary_entry(line):
    key, value = line.split('=>')
    key = key.strip().strip("'")
    if key == '\\\\':
        key = '\\'
    key = key.encode('cp1251')
    assert len(key) == 1, key
    key = int(key[0])

    value = value.strip()
    values = value.split('#', 1)
    value = values[0].strip()  # removes trailing comment
    if len(values) == 2:
        comment = values[1].strip()
    else:
        comment = None
    value = value.rstrip(',')
    chars = [x.strip() for x in value.split('.')]
    assert min(x.startswith('chr(') and x.endswith(')') for x in chars)
    chars = [int(x[4:-1], 0) for x in chars]
    chars = ''.join(chr(x) for x in chars)
    
    return key, chars, comment


if __name__ == '__main__':
    '''Code that generates "decoding_table" from Perl ucs encoding table.

    1. Download Perl UCS encoding table from: 
        https://raw.githubusercontent.com/typiconman/Perl-Lingua-CU/master/lib/Lingua/CU/Scripts/ucsequivs
    2. Put it into current directory.
    3. Run this code to generate Python array "decoding_table"
    '''

    dt, cm = _build_decoding_table('ucsequivs')
    
    print('decoding_table = (')
    for x,c in zip(dt, cm):
        if c is not None:
            c = '  # ' + c
        else:
            c = ''
        if x == "'":  # treat single quote separately to avoid syntax error (is there a better way? - MK)
            print('\t"%s",%s' % (x.encode('unicode-escape').decode(), c))
        else:
            print("\t'%s',%s" % (x.encode('unicode-escape').decode(), c))
    print(')')