# coding: utf-8
'''
Created on Feb 25, 2016

@author: mike
'''
import unittest
from cslavonic.normalize import explode_nfd


class TestNormalize(unittest.TestCase):
    
    def test(self):
        
        nset = set(explode_nfd('ᲂу҆спе́нїю'))
        
        self.assertEqual(nset, {'ѹ҆спе́нїю', 'ѹ҆спе́нїю', '\u1c82у҆спе́нїю', '\u1c82у҆спе́нїю'})


if __name__ =='__main__':
    unittest.main()