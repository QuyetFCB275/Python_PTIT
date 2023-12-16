# Note !




from functools import cmp_to_key

def cmp(a, b):
    s1 = str(a)
    s2 = str(b)
    l1 = [int (x) for x in s1]
    l2 = [int (x) for x in s2]
    if sum(l1) == sum(l2) and a > b:
        return 1
    if sum(l1) > sum(l2):
        return 1
    return -1

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=cmp_to_key(cmp))
    for x in a:
        print(x, end=' ')
    print()