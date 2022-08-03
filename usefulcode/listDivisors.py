def divisors(num):
    div = [1,num]
    i = 2
    while i < num/2+1:
        if num % i == 0:
            div.append(i)
        i += 1
    return div


print(divisors(28))
