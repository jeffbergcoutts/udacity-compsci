def print_numbers(a):
    i = 1
    while i <= a:
        print i
        i = i + 1

print_numbers(3)

def factorial(n):
    t = 1
    while n > 1:
        t = t * n
        n = n - 1
        break

    return t

print factorial(10)
