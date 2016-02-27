'''
Created on Feb 25, 2016

@author: mike
'''
import unittest
from cslavonic.numerals import numeral_string


class TestNumerals(unittest.TestCase):
    
    def test_0_9(self):
        self.assertEquals(numeral_string(0), '0҃')
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
        self.assertEquals(numeral_string(1000), '҂а҃')
        self.assertEquals(numeral_string(1001), '҂а҃а')
        self.assertEquals(numeral_string(1010), '҂а҃і')
        self.assertEquals(numeral_string(1100), '҂а҃р')
        self.assertEquals(numeral_string(1110), '҂ар҃і')
        self.assertEquals(numeral_string(1800), '҂а҃ѿ')

    def test_10000(self):
        self.assertEquals(numeral_string(10000), '҂і҃')
        self.assertEquals(numeral_string(10002), '҂і҃ в҃')
        self.assertEquals(numeral_string(10010), '҂і҃ і҃')
        self.assertEquals(numeral_string(10100), '҂і҃ р҃')
        self.assertEquals(numeral_string(11000), '҂а҃҂і')
        self.assertEquals(numeral_string(11100), '҂а҃і р҃')
        self.assertEquals(numeral_string(10800), '҂і҃ ѿ҃')

    def test_misc(self):
        self.assertEquals(numeral_string(1), 'а҃')
        self.assertEquals(numeral_string(12), 'в҃і')
        self.assertEquals(numeral_string(123), 'рк҃г')
        self.assertEquals(numeral_string(1234), '҂асл҃д')
        self.assertEquals(numeral_string(12345), '҂в҃і тм҃є')
        self.assertEquals(numeral_string(123456), '҂рк҃г ун҃ѕ')
        self.assertEquals(numeral_string(1234567), '҂҂а҃ ҂сл҃д фѯ҃з')
        self.assertEquals(numeral_string(12345678), '҂҂в҃і ҂тм҃є хѻ҃и')
        self.assertEquals(numeral_string(123456789), '҂҂рк҃г ҂ун҃ѕ ѱп҃ѳ')
        self.assertEquals(numeral_string(1234567890), '҂҂҂а҃ ҂҂сл҃д ҂фѯ҃з ѿч҃')
    
    def test_no_titlo(self):
        self.assertEquals(numeral_string(11100, add_titlo=False), '҂аі р')
    
    def test_order_of_teens(self):
        self.assertEquals(numeral_string(111), 'ра҃і')
        self.assertEquals(numeral_string(121), 'рк҃а')
    
    def test_800s(self):
        self.assertEquals(numeral_string(800), 'ѿ҃')
        self.assertEquals(numeral_string(820), 'ѿк҃')
        self.assertEquals(numeral_string(1860), '҂аѿѯ҃')
    
    def test_other(self):
        self.assertNotEquals(numeral_string(1010), numeral_string(11000))
        
        self.assertEquals(numeral_string(1010), '҂а҃і')
        self.assertEquals(numeral_string(11000), '҂а҃҂і')
        

