total = 0
with open('013.txt') as f:
    for line in f:
        total += int(line)

print(str(total)[:10])