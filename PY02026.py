n, m = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()
b = list(set(map(int, input().split())))
b.sort()
if ''.join(str(x) for x in a) == ''.join(str(x) for x in b):
    print("YES")
else:
    print("NO")