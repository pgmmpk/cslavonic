'''
Created on Mar 30, 2016

@author: mike
'''
import unittest
from cslavonic.calendar import get_julian_day, get_calendar, gregorian_to_julian,\
    julian_to_gregorian, day_of_the_week_str, indiction


class TestCalendar(unittest.TestCase):
    
    def test1(self):
    
        jdn = get_julian_day(2016, 3, 30)
        self.assertEquals(jdn, 2457478)
    
        date = get_calendar(jdn)
        self.assertEqual(date, (2016, 3, 30))
    
        date = get_calendar(jdn, julian=True)
        self.assertEqual(date, (2016, 3, 17))
        
        date = gregorian_to_julian(2016, 3, 30)
        self.assertEqual(date, (2016, 3, 17))

        date = julian_to_gregorian(2016, 3, 17)
        self.assertEqual(date, (2016, 3, 30))
        
        date = julian_to_gregorian(1582, 10, 5)
        self.assertEqual(date, (1582, 10, 15))
        
        date = julian_to_gregorian(1000, 10, 5)
        self.assertEqual(date, (1000, 10, 5))
    
        date = gregorian_to_julian(1582, 10, 15)
        self.assertEqual(date, (1582, 10, 5))
        
        date = gregorian_to_julian(1582, 10, 10)
        self.assertEqual(date, (1582, 10, 5))
        
        date = gregorian_to_julian(1582, 10, 6)
        self.assertEqual(date, (1582, 10, 5))
        
        date = gregorian_to_julian(1582, 10, 5)
        self.assertEqual(date, (1582, 10, 5))

        day = day_of_the_week_str(1582, 10, 4)
        self.assertEqual(day, 'Thursday')
        
        day = day_of_the_week_str(2016, 3, 30)
        self.assertEqual(day, 'Wednesday')

        day = day_of_the_week_str(1, 1, 1, from_julian_date=True)
        self.assertEqual(day, 'Saturday')

    def test_indiction(self):
        indict = indiction(2016)
        self.assertEquals(indict, 6)

        indict = indiction(2010)
        self.assertEquals(indict, 15)
