from math import isqrt

def check(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    s = input()
    ans, k = 0, True
    for i in range(len(s)):
        if i % 2 == 0 and int (s[i]) % 2 == 1:
            k = False
            break
        if i % 2 == 1 and int (s[i]) % 2 == 0:
            k = False
            break
        ans += int(s[i])
    if k == True and check(ans):
        print("YES")
    else:
        print("NO")