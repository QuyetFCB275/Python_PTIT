def trans(a:list, m):
    res = []
    for i in range(m):
        res.append([])
    for x in a:
        for i in range(len(x)):
            res[i].append(x[i])
    return res

n, m = map(int, input().split())
a = []
ans = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
    
if n >= m:
    k = n - m
    for i in range(n):
        if i % 2 == 0 and k > 0:
            k -= 1
        else:
            ans.append(a[i])
elif n < m:
    k = m - n
    b = trans(a, m)
    for i in range(m):
        if i % 2 == 1 and k > 0:
            k -= 1
        else:
            ans.append(b[i])
    ans = trans(ans, n)
for x in ans:
    print(*x)            