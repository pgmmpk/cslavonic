#!/usr/local/bin/python3
# coding: utf-8
# adapted from https://github.com/typiconman/fonts-cu/blob/master/codechart.pl
from __future__ import print_function, unicode_literals
import collections
import codecs
import argparse
import unicodedata
import os
import string
from fontTools import ttx


def irange(start, end):
    ''' inclusive range '''
    return list(range(start, end+1))

RangeInfo = collections.namedtuple('RangeInfo', ['name', 'range'])

_RANGES = [
    RangeInfo("Basic Latin",             irange(0x0000,  0x007F)),
    RangeInfo("Latin-1 Supplement",      irange(0x0080,  0x00FF)),
    RangeInfo("Cyrillic",                irange(0x0400,  0x04FF)),
    RangeInfo("Cyrillic Supplement",     irange(0x0500,  0x052F)),
    RangeInfo("Cyrillic Extended A",     irange(0x2DE0,  0x2DFF)),
    RangeInfo("Cyrillic Extended B",     irange(0xA640,  0xA69F)),
    RangeInfo("Cyrillic Extended C",     irange(0x1C80,  0x1C8F)),
    RangeInfo("Greek",                   irange(0x0370,  0x03FF)),
    RangeInfo("Greek Extended",          irange(0x1F00,  0x1FFF)),
    RangeInfo("Glagolitic",              irange(0x2C00,  0x2C5F)),
    RangeInfo("Glagolitic Extended",     irange(0x1E000, 0x1E02F)),
    RangeInfo("Georgian",                irange(0x10A0,  0x10FF)),
    RangeInfo("General Punctuation",     irange(0x2000,  0x206F)),
    RangeInfo("Miscellaneous Symbols",   irange(0x2600,  0x26FF)),
    RangeInfo("Supplemental Punctuation", irange(0x2E00, 0x2E4F)),
    RangeInfo("Combining Diacritical Marks", irange(0x0300, 0x036F)),
    RangeInfo("Combining Diacritical Marks Supplement", irange(0x1DC0, 0x1DFF)),
    RangeInfo("Combining Half Marks",    irange(0xFE20, 0xFE2F)),
    RangeInfo("Byzantine Musical Symbols", irange(0x1D000, 0x1D015)),
    RangeInfo("Miscellaneous Symbols and Pictographs", irange(0x1F310, 0x1F41F)),
    RangeInfo("Miscellaneous Symbols and Pictographs con't", irange(0x1F510, 0x1F54F)),
    RangeInfo("`Open Range' Private Use", irange(0xF400, 0xF4FF)),
    RangeInfo("`Open Range' Private Use (con't)", irange(0xF500, 0xF5FF)),
]

_COMBINERS = {
    0xA674  : "Wide Est",
    0xA675  : "Eight I",
    0xA676  : "Ten I",
    0xA677  : "Combining U",
    0xA67B  : "Omega",
    0xA678  : "Hard Sign",
    0xA67A  : "Soft Sign",
    0xA679  : "Yeru",
    0xA69E  : "Ef",
    0xA69F  : "Iotified E",
    0xFE2E  : "Titlo Left",
    0xFE2F  : "Titlo Right"
} # listing of characters that Unicode::Collate doesn't recognize


def main_codechart(args):
    path = os.path.dirname(args.fontpath)
    fontname, _ = os.path.splitext(os.path.basename(args.fontpath))
    output = os.path.join(path, fontname) + '.tex'
    
    fnt = ttx.TTFont(args.fontpath)
    
    ## this array keeps track of all combining marks that we will need to TEST!
    #marx = {}
    
    _TEMPL_HEAD = string.Template('''\
    \\documentclass{article}
    \\usepackage{fontspec}
    \\usepackage{xcolor}
    \\usepackage{tabu}
    \\usepackage{hyperref}
    \\usepackage{polyglossia}
    \\usepackage[top=0.5in, bottom=0.5in, left=0.5in, right=0.5in]{geometry}
    \\newfontfamily\\glyphfont[Path=./]{${fontname}.otf}
    \\setmainfont[Mapping=tex-text]{Times}
    \\setdefaultlanguage{english}
    \\setotherlanguage{russian} % don't have Church Slavic available yet :(
    
    \\begin{document}
    \\tabulinesep=1.2mm
    ''')
    
    _TEMPL_FONTDOC = string.Template('''\
    \\section{Font Documentation}
    
    \\textbf{Font name}: ${name} \\\\
    \\textbf{Font author}: ${author} \\\\
    \\textbf{Version}: ${version} \\\\
    \\textbf{Copyright information}: ${copyright} \\\\
    
    ''')
    
    _TEMPL_PHRASE = string.Template('''\
    \\section{Font Test} 
    
    {\\glyphfont{\\tiny The quick brown fox jumps over the lazy dog. 1234567890}} \\\\
    {\\glyphfont{\\scriptsize The quick brown fox jumps over the lazy dog. 1234567890}} \\\\
    {\\glyphfont{\\small The quick brown fox jumps over the lazy dog. 1234567890}} \\\\
    {\\glyphfont{The quick brown fox jumps over the lazy dog. 1234567890}} \\\\
    {\\glyphfont{\\large The quick brown fox jumps over the lazy dog. 1234567890}} \\\\
    {\\glyphfont{\\huge The quick brown fox jumps over the lazy dog. 1234567890}} \\\\
    \\begin{russian}
    {\\glyphfont{\\tiny ${phrase} }} \\\\
    {\\glyphfont{\\scriptsize ${phrase}}} \\\\
    {\\glyphfont{\\small ${phrase}}} \\\\
    {\\glyphfont{ ${phrase}}} \\\\
    {\\glyphfont{\\large ${phrase}}} \\\\
    {\\glyphfont{\\huge ${phrase}}} \\\\
    \\end{russian}
    
    ''')
    
    with codecs.open(output, 'w', 'utf-8') as f:
        f.write(_TEMPL_HEAD.substitute(fontname=fontname))
    
        font_copyright = fnt['name'].names[0].string.decode()
        font_name      = fnt['name'].names[1].string.decode()
        font_version   = fnt['name'].names[5].string.decode()
        font_author    = fnt['name'].names[9].string.decode()
        
        f.write(_TEMPL_FONTDOC.substitute(name=font_name, author=font_author, version=font_version, copyright=font_copyright))
    
        if 'Fedorovsk' in font_name:
            phrase = "Хрⷭ҇то́съ вᲂскре́се и҆з ме́ртвыхъ , сме́ртїю сме́рть пᲂпра́въ , и҆ сꙋ́щымъ во грᲂбѣ́хъ живо́тъ дарᲂва́въ ."
        elif 'Menaion' in font_name:
            phrase = "Хрⷭ҇то́съ вᲂскр҃се и҆з̾ ме́ртвыⷯ, сме́ртїю на́ смерть настꙋпѝ, и҆ гро́бымъ живо́тъ дарᲂва̀."
        else:
            phrase = "Хрⷭ҇то́съ воскре́се и҆з̾ ме́ртвыхъ, сме́ртїю сме́рть попра́въ, и҆ сꙋ́щымъ во гробѣ́хъ живо́тъ дарова́въ."
    
        phrase.encode('utf-8')
        b = _TEMPL_PHRASE.substitute(phrase=phrase).encode('utf-8')
        print(type(b))
        f.write(_TEMPL_PHRASE.substitute(phrase=phrase))
        
        f.write('\\clearpage\n')
        
        for range_name, range_ in _RANGES:
            # DOES FONT HAVE ANY GLYPHS IN THIS RANGE?
            HAS_GLYPHS = 0
            for x in range_:
                if x in fnt['cmap'].tables[1].cmap:
                    HAS_GLYPHS += 1
    
            if not HAS_GLYPHS:
                continue
    
            f.write("\\section{%s}\n\n" % range_name)
            numcols = int ( (len(range_) + 15) / 16 ) # number of columns
            tablestart = range_[0]
            width = max(1.05 * (numcols + 1), 4.0); 
        
            f.write("\\begin{tabu} to " + str(width) + "cm {X[r]|")
            for _ in range(numcols):
                f.write("X[c,b]|")
            f.write("}\n\n")
    
            colheaders = [tablestart + i * 16 for i in range(numcols)]
            f.write('&  ' + '  & '.join(("\\tiny{Ux%04x" % x)[:-1] + 'X}' for x in colheaders))
            f.write('\\\\\n\n')
    
            for rowidx in range(tablestart, tablestart + 16):
                line1 = []
                line2 = []
        
                for colidx in range(rowidx, rowidx + 16 * numcols, 16):
                    value = "%04x" % colidx
                    char  = "\\char\"" + ('%04x' % colidx).upper()  # chr($colidx);
                    char_name  = unicodedata.name(chr(colidx), '')
    
                    if colidx in fnt['cmap'].tables[1].cmap:
                        if "COMBINING" in char_name or colidx in _COMBINERS:
                            line1.append("\\vspace{1mm}\\glyphfont{\\Large{\u25CC" + char + "}}")
                            #if 'SIGN' not in name:
                            #    marx.append(char)
                        else:
                            line1.append("\\vspace{1mm}\\glyphfont{\\Large{" + char + "}}")
                    else:
                        line1.append("\\vspace{1mm}\\glyphfont{\\Large{\\ }}")
    
                    line2.append("\\tiny{" + value + "}")
            
                i = '%x' % (rowidx - tablestart)
                f.write("\\hline " + i.upper() + "  & " + ' & '.join(line1) + "\\\\\n")
                f.write(' & ' + " & ".join(line2) + "\\\\\n")
    
            f.write("\\hline\\end{tabu}\n\n")
    
        spec_info = os.path.join(path, fontname + '-specific-info.tex')
        if os.path.exists(spec_info):
            f.write("\\input{" + fontname + "-specific-info.tex}\n")
        
        f.write("\\end{document}\n")
    
    return 0


def main():
    parser = argparse.ArgumentParser(description='Generates TeX file with font code tables')
    parser.add_argument('fontpath', help='path to the font file, e.g. /path/to/my/font.ttf')
    
    args = parser.parse_args()
    
    parser.exit(main_codechart(args))


if __name__ == '__main__':
    main()