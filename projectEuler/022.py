# import string library function
import string

# Storing the value in variable result
alpha = string.ascii_uppercase

print(alpha)


fi = open('022_names.txt', 'r')
names = fi.read().split(',')
total = 0
names = sorted(names)
for i,name in enumerate(names):
    namevalue = 0
    for alphabet in name.strip().replace('"',''):
        namevalue+= alpha.index(alphabet)+1
    total += namevalue * (i+1)
    print(name, namevalue, i+1)

print(total)
