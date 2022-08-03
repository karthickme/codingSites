def divisors(num):
    count = 2
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            count += 2
        i += 1
    if i ** 2 == num:
        count += 1
    return count

print(divisors(28))
