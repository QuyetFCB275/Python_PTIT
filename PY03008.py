n = int(input())
a = [0] * (n+1)

def check(a:list):
    k1, k2 = 0, 0
    for i in range(1, len(a)):
        if a[i] == 1:
            k1 += 1
        elif a[i] == n - 1:
            k2 += 1
        else:
            return False
    if k1 == n - 1 and k2 == 1:
        return True
    return False

for i in range(n-1):
    z = [int(x) for x in input().split()]
    a[z[0]] += 1
    a[z[1]] += 1
    
if check(a):
    print("Yes")
else:
    print("No")