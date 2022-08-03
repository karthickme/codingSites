results = []
for i in range(2,101):
    for j in range(2,101):
        results.append(i ** j)

print(len(set(results)))