from math import*

n = int(input())
a = list(map(int, input().split()))

ans, sum = 0, 100000000000000000

for x in a:
    b = a[:]
    b.remove(x)
    k = 0
    for y in b:
        k += abs(x - y)
    if k < sum:
        sum = k
        ans = x
        
print(sum, ans)