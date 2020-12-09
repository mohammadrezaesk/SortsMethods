a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
m = 0
for j in range(len(a)):
    m = j
    for i in range(j,len(a)):
        if a[i]<a[m]:
            m = i
    c = a[j]
    a[j] = a[m]
    a[m] = c
print(a)