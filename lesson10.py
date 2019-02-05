'''
Solving Problems notes
0. Relax, don't panic
1: What are the inputs?
- what is the set of valid inputs
- check for invalid
- you decide how inputs are represented, strings, object
2: What are the outputs?
3. Understand the relationship between inputs and outputs - Work out some examples

Try to solve the problem without code
Then try to write an algorithm that solves it - can use pseudo code
4. Simple mechanical solution - don't optimize prematurely - make sure it will work
5. Develop incrementaly and test as you go
Write small pieces of code/functionality at a time, know what they do
be confident that they work - test in small pieces - easier to debug
'''

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(y,m):
    DAYS_OF_MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(y) == True and m == 2:
        return (DAYS_OF_MONTHS[m-1]) + 1
    else:
        return DAYS_OF_MONTHS[m-1]

def nextDay(y,m,d):
    """warning this assumes all months have 30 days"""
    if d < daysInMonth(y,m):
        return y, m, d + 1
    else:
        if m < 12:
            return y, m + 1, 1
        else:
            return y + 1, 1, 1

def dateIsBefore(y, m, d, y2, m2, d2):
    if y < y2:
        return True
    elif y == y2:
        if m < m2:
            return True
        elif m == m2:
            if d < d2:
                return True
    else:
        return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    assert not dateIsBefore(y2,m2,d2,y1,m1,d1)

    noOfDays = 0
    y, m, d = y1, m1, d1
    while dateIsBefore(y, m , d, y2, m2, d2):
        noOfDays = noOfDays + 1
        y, m, d = nextDay(y, m, d)
    
    return noOfDays

print nextDay(2012,2,28) # 2012,3,1
print nextDay(2014,4,28) # 2014,4,29
print nextDay(2015,5,30) # 2015,5,31
print nextDay(2016,12,31) # 2017,1,1
print nextDay(2017,1,1) # 2017,1,2

print isLeapYear(1992) #True
print isLeapYear(2000) #True
print isLeapYear(1900) #False

print daysInMonth(2000, 2) #29
print daysInMonth(1900, 2) #28
print daysInMonth(2000, 3) #31

print daysBetweenDates(2012, 2, 15, 2012, 3, 18)
print daysBetweenDates(2013, 2, 15, 2013, 3, 18)
print daysBetweenDates(2018,4,30,2019,3,12)
print daysBetweenDates(2018,4,21,2018,4,21)
print daysBetweenDates(2018,4,30,2018,6,12)
#print daysBetweenDates(2019,4,39,2018,4,30)