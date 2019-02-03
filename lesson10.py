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

Making progress - write small bits of code, test them, know what they do
'''

days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return False

def nextDay(y,m,d):
    """warning this assumes all months have 30 days"""
    if d < 30:
        return y, m, d + 1
    else:
        if m < 12:
            return y, m + 1, 1
        else:
            return y + 1, 1, 1

def isLessThenDate(y, m, d, y2, m2, d2):
    if y < y2:
        return True
    elif m < m2:
        return True
    elif d < d2:
        return True
    else:
        return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    noOfDays = 0
    y, m, d = y1, m1, d1
    while isLessThenDate(y, m , d, y2, m2, d2):
        noOfDays = noOfDays + 1
        y, m, d = nextDay(y, m, d)
    
    return noOfDays

print daysBetweenDates(2012, 2, 15, 2019, 2, 18)
print daysBetweenDates(2018,4,30,2019,3,12)
print daysBetweenDates(2018,4,21,2018,4,22)
print daysBetweenDates(2018,4,30,2018,6,12)
print daysBetweenDates(2018,4,39,2018,4,30)