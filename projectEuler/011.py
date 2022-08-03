arr = []
with open('011.txt') as f:
    for line in f:
        row = line.split(" ")
        row = [int(i) for i in row]
        arr.append(row)


maxprod = 0
for i in range(0, len(arr)-3):
    for j in range(0, len(arr)):
        prod = 1
        for k in range(0, 4):
            prod *= arr[i+k][j]
            # print(i+k, j, arr[i+k][j])
            maxprod = max(prod, maxprod)
        # print(prod)

for i in range(0, len(arr)):
    for j in range(0, len(arr)-3):
        prod = 1
        for k in range(0, 4):
            prod *= arr[i][j+k]
            # print(i,j+k, arr[i][j+k])
            maxprod = max(prod, maxprod)
        # print(prod)


# diagonal  r
for i in range(0, len(arr)-3):
    for j in range(0, len(arr)-3):
        prod = 1
        for k in range(0, 4):
            prod *= arr[i+k][j+k]
            # print(i+k, j+k, arr[i+k][j+k])
            maxprod = max(prod, maxprod)
        # print(prod)

# diagonal  l
for i in range(0, len(arr)-3):
    for j in range(3, len(arr)):
        prod = 1
        for k in range(0, 4):
            prod *= arr[i+k][j-k]
            # print(i+k, j-k, arr[i+k][j-k])
            maxprod = max(prod, maxprod)
        # print(prod)


print(maxprod)
