for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list()
    b.extend(a[k:])
    b.extend(a[0:k])
    for x in b:
        print(x, end=' ')
    print()