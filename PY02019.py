def gcd(x, y):
    while y > 0:
        return gcd(y, x % y)
    return x

n = int(input())
a = list(map(int, input().split()))
a.sort()
van = []
for i in range(n):
    for j in range(i+1, n):
        if gcd(a[i], a[j]) == 1:
            van.append((a[i], a[j]))
for x in van:
    print(x[0], x[1])