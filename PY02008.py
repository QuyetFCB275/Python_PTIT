f = [1] * 1000005
f[0], f[1] = 0, 0
for i in range(2, 1000005):
    if f[i]:
        for j in range(i*2, 1000005, i):
            f[j] = 0
a = [0]
i = 2
while len(a) < 1005:
    if f[i]:
        a.append(i)
    i += 1
    
n, x = map(int, input().split())
for i in range(n+1):
    x += a[i]
    print(x, end=' ')    