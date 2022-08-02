#not efficient works 
done = 0
for i in range(1, 1001):
    for j in range(1, 1001):
        for k in range(1, 1001):
            if i+j+k == 1000:
                if (i*i)+(j*j) == (k*k):
                    print(i*j*k)
                    done =1
                    break
    if done == 1:
        break
