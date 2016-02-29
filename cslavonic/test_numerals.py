# coding: utf-8
'''
Created on Feb 25, 2016

@author: mike
'''
from __future__ import print_function, unicode_literals
import unittest
import random
from cslavonic.numerals import numeral_string, numeral_parse

TO_TEST = [
    (0, '0҃'),
    (1, 'а҃'),
    (2, 'в҃'),
    (3, 'г҃'),
    (4, 'д҃'),
    (5, 'є҃'),
    (6, 'ѕ҃'),
    (7, 'з҃'),
    (8, 'и҃'),
    (9, 'ѳ҃'),
    (10, 'і҃'),
    (11, 'а҃і'),
    (12, 'в҃і'),
    (13, 'г҃і'),
    (14, 'д҃і'),
    (15, 'є҃і'),
    (16, 'ѕ҃і'),
    (17, 'з҃і'),
    (18, 'и҃і'),
    (19, 'ѳ҃і'),
    (1000, '҂а҃'),
    (1001, '҂а҃а'),
    (1010, '҂а҃і'),
    (1100, '҂а҃р'),
    (1110, '҂ар҃і'),
    (1800, '҂а҃ѿ'),
    (10000, '҂і҃'),
    (10002, '҂і҃ в҃'),
    (10010, '҂і҃ і҃'),
    (10100, '҂і҃ р҃'),
    (11000, '҂а҃҂і'),
    (11100, '҂а҃і р҃'),
    (10800, '҂і҃ ѿ҃'),
    (123, 'рк҃г'),
    (1234, '҂асл҃д'),
    (12345, '҂в҃і тм҃є'),
    (123456, '҂рк҃г ун҃ѕ'),
    (1234567, '҂҂а҃ ҂сл҃д фѯ҃з'),
    (12345678, '҂҂в҃і ҂тм҃є хѻ҃и'),
    (123456789, '҂҂рк҃г ҂ун҃ѕ ѱп҃ѳ'),
    (1234567890, '҂҂҂а҃ ҂҂сл҃д ҂фѯ҃з ѿч҃'),

    (111, 'ра҃і'),
    (121, 'рк҃а'),
    (800, 'ѿ҃'),
    (820, 'ѿк҃'),
    (1860, '҂аѿѯ҃'),

    (1010, '҂а҃і'),
    (11000, '҂а҃҂і'),

    (1234567890123, '҂҂҂҂а҃ ҂҂҂сл҃д ҂҂фѯ҃з ҂ѿч҃ рк҃г'),
    (3423000, '҂҂г҃ ҂у҂к҃҂г')
]

class TestNumerals(unittest.TestCase):
    
    def assert_good(self, num, string):
        self.assertEqual(numeral_string(num).replace('\xa0', ' '), string)
        self.assertEqual(numeral_parse(string), num)

    def test_parser_and_formatter(self):
        
        for num, string in TO_TEST:
            self.assert_good(num, string)

    def test_no_titlo(self):
        self.assertEqual(numeral_string(11100, add_titlo=False), '҂аі\xa0р')
    
    def test_other(self):
        self.assertNotEqual(numeral_string(1010), numeral_string(11000))
        
        self.assertEqual(numeral_string(1010), '҂а҃і')
        self.assertEqual(numeral_string(11000), '҂а҃҂і')
    
    def test_crazy(self):
        self.assertEqual(numeral_string(1234567890123), '҂҂҂҂а҃ ҂҂҂сл҃д ҂҂фѯ҃з ҂ѿч҃ рк҃г'.replace(' ', '\xa0'))

    def test_negative(self):
        self.assertEqual(numeral_string(-1010), '-҂а҃і')
    
    def test_all_upto_10000(self):
        
        for i in range(10000):
            j = numeral_parse(numeral_string(i))
            self.assertEqual(i, j)
            j = numeral_parse(numeral_string(i, add_titlo=False))
            self.assertEqual(i, j)

    def test_random(self):

        for _ in range(10000):
            i = random.randint(10000, 10000000)
            j = numeral_parse(numeral_string(i))
            self.assertEqual(i, j)
            j = numeral_parse(numeral_string(i, add_titlo=False))
            self.assertEqual(i, j)


if __name__ == '__main__':
    unittest.main()