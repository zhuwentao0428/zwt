a=[12,33,4,42,11,22,10]
for i in range(len(a)):
    for b in range(len(a)):
        if a[i]<a[b]:
            a[i],a[b]=a[b],a[i]
print(a)





