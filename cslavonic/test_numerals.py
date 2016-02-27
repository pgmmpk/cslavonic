'''
Created on Feb 25, 2016

@author: mike
'''
import unittest
from cslavonic.numerals import numeral_string, numeral_parse


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
    
    def test_crazy(self):
        self.assertEquals(numeral_string(1234567890123), '҂҂҂҂а҃ ҂҂҂сл҃д ҂҂фѯ҃з ҂ѿч҃ рк҃г')

    def test_parse_0_9(self):
        self.assertEquals(numeral_parse('0҃'), 0)
        self.assertEquals(numeral_parse('а҃'), 1)
        self.assertEquals(numeral_parse('в҃'), 2)
        self.assertEquals(numeral_parse('г҃'), 3)
        self.assertEquals(numeral_parse('д҃'), 4)
        self.assertEquals(numeral_parse('є҃'), 5)
        self.assertEquals(numeral_parse('ѕ҃'), 6)
        self.assertEquals(numeral_parse('з҃'), 7)
        self.assertEquals(numeral_parse('и҃'), 8)
        self.assertEquals(numeral_parse('ѳ҃'), 9)

    def test_parse_10_20(self):
        self.assertEquals(numeral_parse('і҃'), 10)
        self.assertEquals(numeral_parse('а҃і'), 11)
        self.assertEquals(numeral_parse('в҃і'), 12)
        self.assertEquals(numeral_parse('г҃і'), 13)
        self.assertEquals(numeral_parse('д҃і'), 14)
        self.assertEquals(numeral_parse('є҃і'), 15)
        self.assertEquals(numeral_parse('ѕ҃і'), 16)
        self.assertEquals(numeral_parse('з҃і'), 17)
        self.assertEquals(numeral_parse('и҃і'), 18)
        self.assertEquals(numeral_parse('ѳ҃і'), 19)
    
    def test_parse_1000(self):
        self.assertEquals(numeral_parse('҂а҃'), 1000)
        self.assertEquals(numeral_parse('҂а҃а'), 1001)
        self.assertEquals(numeral_parse('҂а҃і'), 1010)
        self.assertEquals(numeral_parse('҂а҃р'), 1100)
        self.assertEquals(numeral_parse('҂ар҃і'), 1110)
        self.assertEquals(numeral_parse('҂а҃ѿ'), 1800)

    def test_parse_10000(self):
        self.assertEquals(numeral_parse('҂і҃'), 10000)
        self.assertEquals(numeral_parse('҂і҃ в҃'), 10002)
        self.assertEquals(numeral_parse('҂і҃ і҃'), 10010)
        self.assertEquals(numeral_parse('҂і҃ р҃'), 10100)
        self.assertEquals(numeral_parse('҂а҃҂і'), 11000)
        self.assertEquals(numeral_parse('҂а҃і р҃'), 11100)
        self.assertEquals(numeral_parse('҂і҃ ѿ҃'), 10800)

    def test_parse_misc(self):
        self.assertEquals(numeral_parse('а҃'), 1)
        self.assertEquals(numeral_parse('в҃і'), 12)
        self.assertEquals(numeral_parse('рк҃г'), 123)
        self.assertEquals(numeral_parse('҂асл҃д'), 1234)
        self.assertEquals(numeral_parse('҂в҃і тм҃є'), 12345)
        self.assertEquals(numeral_parse('҂рк҃г ун҃ѕ'), 123456)
        self.assertEquals(numeral_parse('҂҂а҃ ҂сл҃д фѯ҃з'), 1234567)
        self.assertEquals(numeral_parse('҂҂в҃і ҂тм҃є хѻ҃и'), 12345678)
        self.assertEquals(numeral_parse('҂҂рк҃г ҂ун҃ѕ ѱп҃ѳ'), 123456789)
        self.assertEquals(numeral_parse('҂҂҂а҃ ҂҂сл҃д ҂фѯ҃з ѿч҃'), 1234567890)

    def test_parse_no_titlo(self):
        self.assertEquals(numeral_parse('҂аі р'), 11100)
    
    def test_parse_order_of_teens(self):
        self.assertEquals(numeral_parse('ра҃і'), 111)
        self.assertEquals(numeral_parse('рк҃а'), 121)
    
    def test_parse_800s(self):
        self.assertEquals(numeral_parse('ѿ҃'), 800)
        self.assertEquals(numeral_parse('ѿк҃'), 820)
        self.assertEquals(numeral_parse('҂аѿѯ҃'), 1860)
    
    def test_parse_other(self):
        self.assertNotEquals(numeral_parse('҂а҃і'), numeral_parse('҂а҃҂і'))
        
        self.assertEquals(numeral_parse('҂а҃і'), 1010)
        self.assertEquals(numeral_parse('҂а҃҂і'), 11000)
    
    def test_parse_crazy(self):
        self.assertEquals(numeral_parse('҂҂҂҂а҃ ҂҂҂сл҃д ҂҂фѯ҃з ҂ѿч҃ рк҃г'), 1234567890123)
