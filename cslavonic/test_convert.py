# coding: utf-8
from __future__ import print_function, unicode_literals

import unittest
from cslavonic.convert import expand_titlo

class TestConvert(unittest.TestCase):

    def test_expand_titlo(self):

        result = expand_titlo('ꙗ҆́кѡ да бл҃гоꙋгоди́тъ бг҃ꙋ')

        self.assertEqual(result, 'ꙗ҆́кѡ да благоꙋгоди́тъ Бо́гу')

    def test_digit(self):

        result = expand_titlo('а҃\u0456 рк҃г')

        self.assertEqual(result, '11 123')

    def test_more_digits(self):

        result = expand_titlo('\u043f\u0483')
        self.assertEqual(result, '80')

        result = expand_titlo(':\u043f\u0483.')
        self.assertEqual(result, ':80.')

        result = expand_titlo(' \u043f\u0483 ')
        self.assertEqual(result, ' 80 ')

        result = expand_titlo('҂ацп҃а')
        self.assertEqual(result, '1981')

if __name__ == '__main__':
    unittest.main()
