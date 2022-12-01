a=[8,5,3,9]
b=3
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if b==a[i]-a[j]:
            print([a[i],a[j]])