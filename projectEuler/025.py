def fibonacci_generator(b=1):
    a = 0
    while True:
        yield a
        a, b = b, a + b


for i, num in enumerate(fibonacci_generator()):
    if len(str(num)) == 1000:
        print(i)
        break
