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

for i in range(int(input())):
    n = input()
    sum = 0
    for j in n:
        # sum += ord(j) - ord('0')
        sum += int (j)
    if isPrime(sum):
        print("YES")
    else:
        print("NO")