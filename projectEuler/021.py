def divisorssum(num):
    div = [1]
    i = 2
    while i < num/2+1:
        if num % i == 0:
            div.append(i)
        i += 1
    return sum(div)


# print(divisorssum(284))
# print(divisorssum(220))
collection = {}
for i in range(1, 10001):
    collection[i] = divisorssum(i)
    # print(i)

# collection = {9996: 18732, 9997: 783, 9998: 5002,
#             9999: 5913, 10000: 14211, 220: 284, 284: 220}

sum = 0
for k, v in collection.items():
    if k == v:
        continue
    if v in collection.keys():
        if collection[v] == k:
            print(k, v)
            sum += k
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(sum)
