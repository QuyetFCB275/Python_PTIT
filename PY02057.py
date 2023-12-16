n, m = map(int, input().split())
maxx, minn = 0, 999999999
a = []

def solve(b:list):
    for x in b:
        s = str(x)
        if s == s[::-1] and len(s) > 1:
            global maxx
            maxx = max(maxx, x)
            
for i in range(n):
    b = [int(x) for x in input().split()]
    maxx = max(maxx, max(b))
    minn = min(minn, min(b))
    a.append(b)
res = maxx - minn
if sum(row.count(res) for row in a) == 0:
    print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f'Vi tri [{i}][{j}]')