from math import *

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
for i in range(n-1):
    for j in range(i+1, n):
        if isPrime(a[i]) and isPrime(a[j]) and a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(*a)