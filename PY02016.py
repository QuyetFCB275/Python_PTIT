for i in range(int(input())):
    n = int(input())
    dt = {}
    a = list(map(int, input().split()))
    for x in a:
        if x in dt:
            dt[x] += 1
        else:
            dt[x] = 1
    ans, k = 0, 0
    for x in dt:
        if k < dt[x]:
            ans = x
            k = dt[x]
    if k > n / 2:
        print(ans)
    else:
        print("NO")