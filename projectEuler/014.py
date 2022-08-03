

coll = {1: 1}


def Collatz_lenth(n):
    if n in coll.keys():
        return coll[n]
    else:
        if n % 2 == 0:
            coll[n] = Collatz_lenth(n/2) + 1
        else:
            coll[n] = Collatz_lenth(3*n + 1) + 1
    return Collatz_lenth(n)


# print(Collatz_lenth(13))
# print("--------")
# print(coll)
longnum = 1
nu = 1
for i in range(1000001, 28, -1):
    temp = Collatz_lenth(i)
    if longnum < temp:
        nu = i
        longnum = temp
        print(i, "--", longnum)

print("--------")
print(longnum)
print(nu)
print("--------")

# max_nu = max(coll, key=coll.get)
# print(max_nu)
