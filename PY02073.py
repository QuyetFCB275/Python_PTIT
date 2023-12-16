for i in range(int(input())):
    n = int(input())
    x, y, z = map(int, input().split())
    f = [0] * 105
    f[1] = x
    if x < z:
        f[2] = x + x
    else:
        f[2] = x + z
    for i in range(3, 104):
        f[i] = f[i-1] + x
        if i % 2 == 0:
            f[i] = min(f[i], f[i//2] + z)
        else:
            f[i] = min(f[i], f[i//2 + 1] + y + z)
    print(f[n])