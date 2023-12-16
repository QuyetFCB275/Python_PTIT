from math import*

n, k = map(int, input().split())
dem = 0
for x in range(int(pow(10, k-1)), int(pow(10, k))):
    if gcd(n, x) == 1:
        dem += 1
        print(x, end=' ')
        if dem == 10:
            print()
            dem = 0