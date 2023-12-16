from math import isqrt

def isPrime(x:int):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = [] * n
maxx = 0
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
    for x in b:
        if isPrime(x):
            maxx = max(maxx, x)
if maxx == 0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print(f'Vi tri {[i]}{[j]}')