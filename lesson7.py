print 'def weekend(day)'
def weekend(day):
    if day == 'Saturday':
        return True
    elif day == 'Sunday':
        return True
    else:
        return False

print weekend('Monday')
print weekend('Saturday')
print weekend('July')

print 'stamps(n)'
def stamps_old(n):
    five = n//5
    two = (n-(five*5))//2
    one = n-((two*2)+(five*5))
    return (five, two, one)

def stamps(n):
    remaining_value = n
    five = n//5
    remaining_value = n%5
    two = remaining_value//2
    remaining_value = remaining_value%2
    one = remaining_value
    return (five, two, one)

print stamps(8)
print stamps(5)
print stamps(29)
print stamps(0)

print 'def set_range()'
def set_range(first, second, third):
    biggest = max(first, second, third)
    smallest = min(first, second, third)
    return biggest - smallest

print set_range(10, 4, 7)
print set_range(1.1, 7.4, 18.7)
