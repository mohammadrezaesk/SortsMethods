a = input().split(" ")
a[0] = int(a[0])
m = a[0]
for i in range(1,len(a)):
    a[i] = int(a[i])
    if a[i]>m:
        m = a[i]
b = [ 0 for x in range(m+1) ]
for i in a:
    b[i] += 1
c = []
j = 0
while len(c)<len(a):
    for i in range(b[j]):
        c.append(j)
    j += 1
print(c)