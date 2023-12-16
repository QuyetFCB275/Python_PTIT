from math import gcd, isqrt

def check(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    ans = 0
    for x in range(1, n):
        if gcd(x, n) == 1: ans += 1
    if check(ans):
        print("YES")
    else: print("NO")