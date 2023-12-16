for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(n):
        a.append(int(input()))
    ans, k = 0, 0
    for x in a:
        if k < a.count(x):
            ans, k = x, a.count(x)
        if k == a.count(x):
            ans = min(ans, x)
    print(ans)