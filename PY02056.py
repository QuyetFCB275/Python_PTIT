n, m = map(int, input().split())
maxx = 0
a = []

def solve(b:list):
    for x in b:
        s = str(x)
        if s == s[::-1] and len(s) > 1:
            global maxx
            maxx = max(maxx, x)
            
for i in range(n):
    b = [int(x) for x in input().split()]
    solve(b)
    a.append(b)
if maxx == 0:
    print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print(f'Vi tri [{i}][{j}]')