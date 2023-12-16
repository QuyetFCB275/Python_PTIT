s = input()
k = int(input())
dt = {}
x = ""
for i in s:
    x += i
    if len(x) == 2:
        if int(x) not in dt:
            dt[int(x)] = 1
        else:
            dt[int(x)] += 1
        x = ""
a = list(dt.keys())
a.sort()
kt = True
for x in a:
    if dt[x] >= k:
        kt = False
        print(x, dt[x])
if kt:
    print("NOT FOUND")