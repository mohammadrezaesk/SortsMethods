def insertToSorted(a, n):
    b = []
    flag = 0
    for i in range(len(a)):
        if a[i]>n:
            b = a[:i] + [n] + a[i:]
            flag = 1
            break
    if not flag:
        b = a + [n]
    return b

a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(1,len(a)):
    a[:i+1] = insertToSorted(a[:i], a[i])
print(a)
