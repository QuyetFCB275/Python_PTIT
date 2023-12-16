for i in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        v = list(map(int, input().split()))
        a.append(v)
    b = []
    for i in range(3):
        v = list(map(int, input().split()))
        b.append(v)
    k1 = n - 3
    k2 = m - 3
    ans = 0
    for i in range(k1 + 1):
        for j in range(k2 + 1):
            ans += a[0 + i][0 + j] * b[0][0]
            ans += a[0 + i][1 + j] * b[0][1]
            ans += a[0 + i][2 + j] * b[0][2]
            ans += a[1 + i][0 + j] * b[1][0]
            ans += a[1 + i][1 + j] * b[1][1]
            ans += a[1 + i][2 + j] * b[1][2]
            ans += a[2 + i][0 + j] * b[2][0]
            ans += a[2 + i][1 + j] * b[2][1]
            ans += a[2 + i][2 + j] * b[2][2]
    print(ans)