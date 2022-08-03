def fibonacci_generator(b=1):
    a = 0
    while True:
        yield a
        a, b = b, a + b


fi = fibonacci_generator()
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))
print(next(fi))

