sum = 0
for i in range(2, 1000000):
    temp = 0
    for j in str(i):
        temp += int(j)**5
    if temp == i:
        print(i)
        sum += temp
print(sum)