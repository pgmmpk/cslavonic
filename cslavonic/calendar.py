'''
Created on Mar 29, 2016

Converts Julian date to Gregorian date and vv

Code based on algorithms from: https://en.wikipedia.org/wiki/Julian_day
These algorithms were adjusted to assume that before the inception of Gregorian calendar there was
a single calendar (i.e. Gregorian calendar before Oct 5 1582 was identical to Julian.

@author: mike
'''


GREGORIAN_INCEPTION_AS_GREGORIAN_DATE = (1582, 10, 15)
GREGORIAN_INCEPTION_AS_JULIAN_DATE = (1582, 10, 5)

def get_julian_day(year, month, day, from_julian_date=False):
    assert 1 <= month <= 12
    assert 1 <= day <= 31

    # before Gregorian reform calendars are assumed to be identical
    if not from_julian_date and (year, month, day) < GREGORIAN_INCEPTION_AS_GREGORIAN_DATE:
        if (year, month, day) > GREGORIAN_INCEPTION_AS_JULIAN_DATE:
            year, month, day = GREGORIAN_INCEPTION_AS_JULIAN_DATE
        from_julian_date = True

    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    
    if from_julian_date:
        jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
    else:
        jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    
    return jdn

def get_calendar(jdn, julian=False):
    
    if julian:
        f = jdn + 1401
    else:
        f = jdn + 1401 + (((4 * jdn + 274277) // 146097) * 3) // 4 - 38

    e = f * 4 + 3
    g = (e % 1461) // 4
    h = 5 * g + 2
    
    day = (h % 153) // 5 + 1
    month = ( h // 153 + 2 ) % 12 + 1
    year = e // 1461 - 4716 + (14 - month) // 12
    
    return year, month, day

def julian_to_gregorian(year, month, day):
    if (year, month, day) < GREGORIAN_INCEPTION_AS_JULIAN_DATE:
        return year, month, day
    jdn = get_julian_day(year, month, day, from_julian_date=True)
    return get_calendar(jdn, julian=False)

def gregorian_to_julian(year, month, day):
    if (year, month, day) < GREGORIAN_INCEPTION_AS_GREGORIAN_DATE:
        if (year, month, day) > GREGORIAN_INCEPTION_AS_JULIAN_DATE:
            return GREGORIAN_INCEPTION_AS_JULIAN_DATE
        return year, month, day
    jdn = get_julian_day(year, month, day, from_julian_date=False)
    return get_calendar(jdn, julian=True)


def day_of_the_week(year, month, day, from_julian_date=False):
    jdn = get_julian_day(year, month, day, from_julian_date=from_julian_date)
    return (jdn + 1) % 7  # 0-Sun, 1-Mon, 2-Tue, 3-Wed, 4-Thu, 5-Fri, 6-Sat

def day_of_the_week_str(year, month, day, from_julian_date=False):
    return ['Sunday', 
            'Monday', 
            'Tuesday', 
            'Wednesday', 
            'Thursday',
            'Friday', 
            'Saturday'][day_of_the_week(year, month, day, from_julian_date=from_julian_date)]

def indiction(year):
    i = year % 15
    if i == 0:
        i = 15
    return i


if __name__ == '__main__':
    
    jdn = get_julian_day(2016, 3, 30)
    print(jdn)
    print(get_calendar(jdn))
    print(get_calendar(jdn, julian=True))
    
    print(gregorian_to_julian(2016, 3, 30))
    print(julian_to_gregorian(2016, 3, 17))
    
    print(julian_to_gregorian(1582, 10, 5))
    print(julian_to_gregorian(1000, 10, 5))
    print(gregorian_to_julian(1000, 10, 5))

    print(gregorian_to_julian(1582, 10, 15))
    print(gregorian_to_julian(1582, 10, 10))
    print(gregorian_to_julian(1582, 10, 6))
    print(gregorian_to_julian(1582, 10, 5))
    print(day_of_the_week_str(1582, 10, 4))
    print(day_of_the_week_str(2016, 3, 30))
    print(day_of_the_week_str(1, 1, 1, from_julian_date=True))
