def getFibonacci():
    a, b = 0, 1

    while True:
        yield b
        b = a + b
        a = b - a


result = []

for num in getFibonacci():
    if num > 4000000:
        break
    if num%2==0:
        result.append(num)

print(sum(result))
