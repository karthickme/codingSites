# Increment value should be a LCM of the prime numbers
primes = [2, 3, 5, 7, 11, 13, 17, 19]
inc = 1
for i in primes:
    inc *= i

# function to check if the nubmer is devisiable by all the numbers


def divCheck(num):
    for i in range(3, 20):
        if num % i != 0:
            return False
    return True


# going to each of number based on the increment value set earlier
index = inc

while True:
    if divCheck(index):
        print("------------------end------------------")
        break
    index += inc
    print(index)
