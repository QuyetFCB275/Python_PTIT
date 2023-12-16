import math

def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    sqr = int(math.sqrt(n))
    for i in range (5, sqr + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def check(n):
    if not isPrime(len(n)):
        return False
    cnt = 0
    for i in n:
        if isPrime(ord(i) - ord('0')):
            cnt += 1
    return cnt > len(n) - cnt

for i in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")