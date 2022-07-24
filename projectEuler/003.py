import math

numbeer = 600851475143


def isprime(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a+1
    return num > 1


factors = []


def fasts(n):
    f = 1
    while f * f <= n:
        if n % f == 0:
            factors.append(f)
            f = f + 1

        else:
            f = f + 1


fasts(numbeer)
print(factors)

result = 0
for i in factors:
    if isprime(i):
        result = i
print(result)
