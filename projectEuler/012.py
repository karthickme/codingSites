def triNum():
    i = 1
    sum = 0
    while True:
        sum += i
        i += 1
        yield sum

# This take 5 mins to run!! no efficient
# def countDivisers(num):
#     count = 2
#     for i in range(2, int(num/2)+1):
#         if num % i == 0:
#             count += 1
#     return count


def countDivisers(num):
    count = 2
    i = 2
    while i ** 2 < num:
        if num % i == 0:
            count += 2
        i += 1
    if i ** 2 == num:
        count += 1
    return count


# print(countDivisers(28))

tr = triNum()
tri = next(tr)
while True:
    tri = next(tr)
    if tri % 28 != 0:
        continue
    count = countDivisers(tri)
    print(tri, count)
    if count > 500:
        print("++++++++++++++++++++++++++++++++")
        print(tri)
        break


# for i in range(1, 10):
#     print(next(tr))
