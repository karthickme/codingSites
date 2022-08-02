import math


def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a+1
    return num > 1

totalSum = 2
for i in range(3, 2000001,2):
    if isprime(i):
        totalSum+= i

print(totalSum)
