from math import factorial

def Krish(n):
    ans = 0
    while n:
        k = n % 10
        ans += factorial(k)
        n //= 10
    return ans

for i in range(int(input())):
    n = int(input())
    if n == Krish(n):
        print("Yes")
    else: print("No")