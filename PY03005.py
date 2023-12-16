def check(s):
    for x in s:
        if not x.isalnum():
            return False
    return True

a = {}
n, k = map(int, input().split())
for i in range(n):
    b = input().lower().split()
    separator = ['.', ',', '/', '?', '!', ':', ';', '-', '(', ')']
    for sep in separator:
        b = [item for x in b for item in x.split(sep)]
    for x in b:
        if len(x) > 0 and check(x):
            if x in a:
                a[x] += 1
            else:
                a[x] = 1
c = []
for items in a.items():
    c.append(items)
c.sort(key=lambda x : (-x[1], x[0]))
for x in c:
    if x[1] >= k:
        print(x[0], x[1])