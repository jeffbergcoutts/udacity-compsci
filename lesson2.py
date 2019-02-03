def printResult(n):
    return n * 1.0

# print printResult(10)

def sum(a, b):
    a = a + b

a = 5
sum(a, 2)
# print a

def is_friend(name):
    return name[0] == 'd'
# print is_friend("Jeff")
# print is_friend("Dave")
# print is_friend("dave")

def biggest(a, b, c):
    if a > b and a > c:
        return a
    elif c > a and c > b:
        return c
    else:
        return "shrug"

print biggest(3, 6, 9)
