from functools import cmp_to_key

def cmp(a, b):
    s1 = str(a)
    s2 = str(b)
    ans1, ans2 = 1, 1
    for x in s1:
        ans1 *= int (x)
    for x in s2:
        ans2 *= int (x)
    if ans1 == ans2 and a > b or ans1 > ans2:
        return 1
    return -1

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x, end=' ')
    print()