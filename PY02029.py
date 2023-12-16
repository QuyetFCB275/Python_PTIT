n, m = map(int, input().split())
dt = {}
inp = [int(x) for x in input().split()]
for x in inp:
    if x in dt:
        dt[x] += 1
    else:
        dt[x] = 1

b = list(set(dt.values()))
b.sort(reverse=True)

if len(b) == 1:
    print("NONE")
else:
    for x in dt.keys():
        if dt[x] == b[1]:
            print(x)
            break