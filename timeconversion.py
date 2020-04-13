#!/bin/python3

''''Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.'''

def timeConversion(s):
    if('PM' in s):
        s = s[:len(s)-2]
        value = int(s[0:2])
        if(value<12):
            return str(value+12)+s[2:]
        return str(value)+s[2:]
    else:
        s = s[:len(s)-2]
        value = (int(s[0:2]))%12
        if(len(str(value))==1):
            val = '0'+str(value)
        return val+s[2:]
 
print(timeConversion('01:00:45AM'))