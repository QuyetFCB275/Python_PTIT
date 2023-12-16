from math import*

ans = 0
a = [1] * 2000005
a[0] = a[1] = 0
for i in range(2, 2000005):
    if a[i]:
        for j in range(2*i, 2000005, i):
            a[j] = 0
            
for i in range(int(input())):
    n = int(input())
    if n <= 3:
        ans += n
        continue
    for j in range(2, isqrt(n)+1):
        while n % j == 0:
            ans += j
            n //= j
        if a[n]:
            ans += n
            break
print(ans)