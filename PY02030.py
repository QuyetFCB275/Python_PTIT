from math import isqrt

def isPrime(x:int):
    if x < 2:
        return False
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
res = []
for x in a:
    if x not in res:
        res.append(x)
        
k = True
for i in range(0, len(res)):
    if isPrime(sum(res[:i+1])) and isPrime(sum(res[i+1:])):
        print(i)
        k = False
        break
if k:
    print("NOT FOUND")