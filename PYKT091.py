def check(s:str):
    if s == s[::-1]:
        return True
    return False

a = []
with open('VANBAN.in', 'r') as file:
    for line in file:
        a.extend(line.strip().split())

ans = []
k = 0
for x in a:
    if check(x):
        if len(x) == k:
            ans.append(x)
        elif len(x) > k:
            k = len(x)
            ans.clear()
            ans.append(x)
dt = {}
for x in ans:
    if x in dt:
        dt[x] += 1
    else:
        dt[x] = 1
for x in dt.keys():
    print(x, dt[x])