def duplicate_encode(word):
    # your code here
    wordvalue = {}
    for i in word:
        if i.lower() in wordvalue:
            wordvalue[i] = ")"
        else:
            wordvalue[i] = "("
    return "".join([wordvalue[i] for i in word])


a = duplicate_encode("recede")
print(a)
# , "()()()"))
