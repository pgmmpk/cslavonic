'''
Created on Feb 25, 2016

@author: mike
'''
import unittest
from cslavonic.normalize import explode_nfd


class TestNormalize(unittest.TestCase):
    
    def test(self):
        
        nset = set(explode_nfd('ᲂу҆спе́нїю'))
        
        self.assertEquals(nset, {})