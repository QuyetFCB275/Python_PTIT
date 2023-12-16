v = {"Xe_con 5" : 10000, "Xe_con 7" : 15000, "Xe_tai 2" : 20000, "Xe_khach 29" : 50000, "Xe_khach 45" : 70000}

dt = {}
for i in range(int(input())):
    a = list(input().split())
    if a[3] == "IN":
        date = a[4] + ":"
        id = a[1] + " " + a[2]
        if date in dt:
            dt[date] += v[id]
        else:
            dt[date] = v[id]
for x in dt.keys():
    print(x, dt[x])