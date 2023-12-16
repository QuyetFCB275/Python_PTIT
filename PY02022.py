f = [1] * 1000005
f[0], f[1] = 0, 0
for i in range(2, 1000005):
    if f[i]:
        for j in range(i*2, 1000005, i):
            f[j] = 0
n = int(input())
a = list(map(int, input().split()))
dt = {}
for x in a:
    if f[x]:
        if x in dt:
            dt[x] += 1
        else:
            dt[x] = 1
for i in dt:
    print(i, dt[i]) 