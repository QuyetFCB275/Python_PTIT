for i in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b, c = [], []
    for x in a:
        if x < 0:
            b.append(x)
        else:
            c.append(x)
    result = b + c
    result.insert(result.index(max(result)), m)
    print(*result)