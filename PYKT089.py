n = int(input())
a = []
while len(a) < n:
    a.extend(map(int, input().split()))

c = [x for x in a if x % 2 == 0]
l = [x for x in a if x % 2 == 1]
c.sort(reverse=False)
l.sort(reverse=True)

i, j = 0, 0

for x in a:
    if x % 2 == 0:
        print(c[i], end=' ')
        i += 1
    else:
        print(l[j], end=' ')
        j += 1