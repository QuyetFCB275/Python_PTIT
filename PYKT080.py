m, n = map(int, input().split())
a = []
b = [0] * (n+2)
a.append(b)
vs = [[False for i in range(n+2)] for j in range(m+2)]

for i in range(n):
    res = [int(x) for x in input().split()]
    res.insert(0, 0)
    res.insert(len(res), 0)
    a.append(res)
a.append(b)

ans = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if a[i][j] == -1:
            for v1 in range(i-1, i+2):
                for v2 in range(j-1, j+2):
                    if v1 == i and v2 == j:
                        continue
                    if not vs[v1][v2]:
                        ans += a[v1][v2]
                        vs[v1][v2] = True

print(ans)