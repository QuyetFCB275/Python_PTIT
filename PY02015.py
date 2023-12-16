a = list(map(int, input().split()))
while a.count(0) < 4:
    ans = 0
    while a.count(a[0]) < 4:
        v = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3] - v)
        ans += 1
    print(ans)
    a.clear()
    a = list(map(int, input().split()))