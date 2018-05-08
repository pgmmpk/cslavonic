# coding: utf-8
from __future__ import print_function, unicode_literals
import unittest
from cslavonic.tokenize import tokenize

class TestNumerals(unittest.TestCase):

    def test_smoke(self):
        out = list(tokenize('Чи́нъ ѡ҆свѧще́нїѧ колесни́цы.'))

        self.assertEqual(out, ['Чи́нъ', ' ', 'ѡ҆свѧще́нїѧ', ' ', 'колесни́цы', '.'])

    def test_spaces(self):
        out = list(tokenize('Чи́нъ  ѡ҆свѧще́нїѧ \t\tколесни́цы.\n'))

        self.assertEqual(out, ['Чи́нъ', '  ', 'ѡ҆свѧще́нїѧ', ' \t\t', 'колесни́цы', '.', '\n'])

    def test_numerals(self):
        out = list(tokenize('blah 10 10.23 11,234 2,234,567.99 blah'))

        self.assertEqual(out, ['blah', ' ', '10', ' ', '10.23', ' ', '11,234', ' ', '2,234,567.99', ' ', 'blah'])

    def test_cu_numerals(self):
        out = list(tokenize('blah ҂асл҃д'))

        self.assertEqual(out, ['blah', ' ', '҂асл҃д'])

    def test_titlo(self):
        out = list(tokenize('ꙗ҆́кѡ да бл҃гоꙋгоди́тъ бг҃ꙋ,'))
        self.assertEqual(out, ['ꙗ҆́кѡ', ' ', 'да', ' ', 'бл҃гоꙋгоди́тъ', ' ', 'бг҃ꙋ', ','])

    def test_unnormalized(self):
        out = list(tokenize('по́мощи, нижѐ  тѧжча́йшагѡ'))
        self.assertEqual(out, ['по́мощи', ',', ' ', 'нижѐ', '  ', 'тѧжча́йшагѡ'])

    def test_small_letters(self):
        out = list(tokenize('ꙗ҆́кѡ новосажᲁе́нїѧ ма̑сличнаѧ'))
        self.assertEqual(out, ['ꙗ҆́кѡ', ' ', 'новосажᲁе́нїѧ', ' ', 'ма̑сличнаѧ'])

    def test_greek_polytonic(self):
        out = list(tokenize('γλωσσαλγία'))
        self.assertEqual(out, ['γλωσσαλγία'])


if __name__ == '__main__':
    unittest.main()
