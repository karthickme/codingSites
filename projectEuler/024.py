# A Python program to print all
# permutations using library function
from itertools import permutations


# Get all permutations of [1, 2, 3]
perm = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

# print(perm[1000000-1])
for i in perm[1000000-1]:
    print(i,end="")
