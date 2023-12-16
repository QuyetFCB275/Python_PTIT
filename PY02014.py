import bisect

a = [1] * 10005
a[0] = a[1] = 0
for i in range(2, 10005):
    if a[i] == 1:
        for j in range(i*2, 10005, i):
            a[j] = 0
prime = []
for i in range(2, 10005):
    if a[i]:
        prime.append(i)

n = int(input())
res = list(map(int, input().split()))
count = 0
for x in res:
    if a[x] == 0:
        idx = bisect.bisect_right(prime, x)
        count = max(count, min(prime[idx] - x, x - prime[idx-1]))
print(count)