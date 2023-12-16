from math import gcd

for t in range(int(input())):
    n, k = map(int, input().split())
    a = []
    while len(a) < n:
        # a.append(map(int, input().split()))
        b = list(map(int, input().split()))
        a.extend(b)
    result = []
    for i in range(n):
        m = a[i]
        for j in range(i, n):
            if a[j] % k != 0:
                break
            
            m = gcd(m, a[j])
            if m == k:
                result.append(j-i+1)
                break
            
    if len(result) == 0:
        print(-1)
    else:
        print(min(result))