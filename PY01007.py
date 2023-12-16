for i in range(int(input())):
    n, x, m = map(float, input().split())
    k = (100 + x) / 100
    for j in range(1, 200):
        if n * (k ** j) >= m:
            print(j)
            break