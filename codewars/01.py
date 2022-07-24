def create_phone_number(n):
    num = ""
    for i in n:
        num = num+str(i)
    return f"({num[0:3]}) {num[3:6]}-{num[6:10]}"


a = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

print(a)
