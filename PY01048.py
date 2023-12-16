from math import *

for i in range(int(input())):
    n = int(input())
    ans = 0
    for j in range(2, isqrt(2*n) + 1):
        if (j % 2 == 0 and n / j == n//j + 0.5) or (j % 2 == 1 and n % j == 0):
            k = n / j
            if j / 2 < k:
                ans += 1
    print(ans)