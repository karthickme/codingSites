
def palCheck(n):
    strnum = str(n)
    for i, j in enumerate(strnum):
        length = len(strnum)-1
        if strnum[i] != strnum[length-i]:
            return False
    return True


big_product = 0
x = 0
y = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        number = i * j
        if(palCheck(number)):
            if big_product < number:
                big_product = number
                x = i
                y = j
                continue

print(big_product)
print(x, y)
