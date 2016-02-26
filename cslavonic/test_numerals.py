'''
Created on Feb 25, 2016

@author: mike
'''
import unittest
from cslavonic.numerals import numeral_string


class TestNumerals(unittest.TestCase):
    
    def test_0_9(self):
        self.assertEquals(numeral_string(0), '')
        self.assertEquals(numeral_string(1), 'а҃')
        self.assertEquals(numeral_string(2), 'в҃')
        self.assertEquals(numeral_string(3), 'г҃')
        self.assertEquals(numeral_string(4), 'д҃')
        self.assertEquals(numeral_string(5), 'є҃')
        self.assertEquals(numeral_string(6), 'ѕ҃')
        self.assertEquals(numeral_string(7), 'з҃')
        self.assertEquals(numeral_string(8), 'и҃')
        self.assertEquals(numeral_string(9), 'ѳ҃')

    def test_10_20(self):
        self.assertEquals(numeral_string(10), 'і҃')
        self.assertEquals(numeral_string(11), 'а҃і')
        self.assertEquals(numeral_string(12), 'в҃і')
        self.assertEquals(numeral_string(13), 'г҃і')
        self.assertEquals(numeral_string(14), 'д҃і')
        self.assertEquals(numeral_string(15), 'є҃і')
        self.assertEquals(numeral_string(16), 'ѕ҃і')
        self.assertEquals(numeral_string(17), 'з҃і')
        self.assertEquals(numeral_string(18), 'и҃і')
        self.assertEquals(numeral_string(19), 'ѳ҃і')
    
    def test_1000(self):
        self.assertEquals(numeral_string(1000), '҂а')
        self.assertEquals(numeral_string(1001), '҂а҃а')
        self.assertEquals(numeral_string(1010), '҂а҃і')
        self.assertEquals(numeral_string(1100), '҂а҃р')
        self.assertEquals(numeral_string(1110), '҂ар҃і')
        self.assertEquals(numeral_string(1800), '҂а҃ѿ')

    def test_10000(self):
        self.assertEquals(numeral_string(10000), '҂і')
        self.assertEquals(numeral_string(10002), '҂і в҃')
        self.assertEquals(numeral_string(10010), '҂і і҃')
        self.assertEquals(numeral_string(10100), '҂і р҃')
        self.assertEquals(numeral_string(11100), '҂аі р҃')
        self.assertEquals(numeral_string(10800), '҂і ѿ҃')

    def test_misc(self):
        self.assertEquals(numeral_string(1), 'а҃')
        self.assertEquals(numeral_string(12), 'в҃і')
        self.assertEquals(numeral_string(123), 'рк҃г')
        self.assertEquals(numeral_string(1234), '҂асл҃д')
        self.assertEquals(numeral_string(12345), '҂ві тм҃є')
        self.assertEquals(numeral_string(123456), '҂ркг ун҃ѕ')
        self.assertEquals(numeral_string(1234567), '҂҂аслд фѯ҃з')
        self.assertEquals(numeral_string(12345678), '҂҂ві тмє хѻ҃и')
        self.assertEquals(numeral_string(123456789), '҂҂ркг унѕ ѱп҃ѳ')
        self.assertEquals(numeral_string(1234567890), '҂҂҂аслд фѯз ѿ҃ч')
    
    def test_to_titlo(self):
        self.assertEquals(numeral_string(11100, add_titlo=False), '҂аі р')