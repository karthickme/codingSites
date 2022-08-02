import math


def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a+1
    return num > 1


# incrementing by 2 as even cannot be prime
num = 10000  # using 1 less as we are takein 2 as prime
i = 1
while num != 0:
    i += 2
    if isprime(i):
        num -= 1


print(i)
