a = [1] * 10005
a[0] = a[1] = 0
for i in range(10005):
    if a[i] :
        for j in range(i*2, 10005, i):
            a[j] = 0
n, m = map(int, input().split())
ans = []
for i in range(n):
    tmp = list(map(int, input().split()))
    b = [1 if a[x] == 1 else 0 for x in tmp]
    ans.append(b)
for x in ans:
    print(*x)