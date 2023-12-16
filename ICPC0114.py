from math import*

def kt(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    a, b, sum = n, 0, 0
    while n :
        k = n % 10
        sum += k
        b = b * 10 + k
        n //= 10
        if k != 2 and k != 3 and k != 5 and k != 7:
            return False
    if kt(sum) and kt(a) and kt(b):
        return True
    return False

for i in range(int(input())):
    n = int(input())
    if check(n):
        print("Yes")
    else: print("No")