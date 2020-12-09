def mergeSorted(a,b):
    c = []
    ai = 0
    bi = 0
    while ai<len(a) and bi<len(b):
        if a[ai]<b[bi]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1
    while ai<len(a):
        c.append(a[ai])
        ai += 1
    while bi<len(b):
        c.append(b[bi])
        bi += 1   
    return c
def mergeSort(a):
    if len(a)==1:
        return a
    mid = len(a)//2
    return mergeSorted(mergeSort(a[:mid]),mergeSort(a[mid:]))

a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
print(mergeSort(a))
