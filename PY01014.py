a, k, n = map(int, input().split())
x = k - (a % k)
if x == 0:
    x = k
if a + x > n:
    print(-1)
else:
    while x <= n - a:
        print(x, end=' ')
        x += k