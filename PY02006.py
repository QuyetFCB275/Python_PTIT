def check(a, b):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if check(a, b):
        print("YES")
    else: print("NO")