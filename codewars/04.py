def spin_words(sentence):
    # Your code goes here
    returnitem = ""
    for i in sentence.split(" "):
        if len(i) > 5 :
            i = i[::-1]
        returnitem = returnitem + i + " "
    return returnitem.strip()


a = spin_words("letters included present Write reversed and be only included returns five returns")
"srettel dedulcni tneserp Write desrever and be only dedulcni snruter five snruter"
"srettel dedulcni tneserp etirW desrever and be only dedulcni snruter five snruter"