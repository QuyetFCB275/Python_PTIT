n = int(input())
a = []
while len(a) < n:
    a.extend(list(map(int, input().split())))
    
b = [x for x in a if x % 2 == 0]
c = [x for x in a if x % 2 == 1]
b.sort()
c.sort(reverse=True)

i, j = 0, 0
for x in a:
    if x % 2 == 0:
        print(b[i], end=' ')
        i+=1
    else:
        print(c[j], end=' ')
        j+=1