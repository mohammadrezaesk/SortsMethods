import random
def qucikSort(a):
    if len(a) <= 1:
        return a
    pivot = random.randrange(0,len(a)-1)
    l = []
    r = []
    m = []
    for i in a:
        if i<a[pivot]:
            l.append(i)
        elif i == a[pivot]:
            m.append(i)
        else:
            r.append(i)
    return qucikSort(l) + m + qucikSort(r)
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
print(qucikSort(a))
