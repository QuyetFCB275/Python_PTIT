from math import isqrt

n = input()
a = list(map(int, input().split()))
b = []
for x in a:
    if x not in b:
        b.append(x)
# print(*b)

def check(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

k = False
for i in range(len(b)):
    m = b[:i+1]
    n = b[i+1:]
    if check(sum(m)) and check(sum(n)):
        print(i)
        k = True
        break
if not k:
    print("NOT FOUND")