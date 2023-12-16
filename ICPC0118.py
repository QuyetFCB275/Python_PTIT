a = ['Bach Duong', 'Kim Nguu', 'Song Tu', 'Cu Giai', 'Su Tu', 'Xu Nu', 'Thien Binh', 'Thien Yet', 'Nhan Ma', 'Ma Ket', 'Bao Binh', 'Song Ngu']

for i in range(int(input())):
    d, m = map(int, input().split())
    if m == 1:
        if d <= 19: print(a[9])
        else: print(a[10])
    elif m == 2:
        if d <= 18: print(a[10])
        else: print(a[11])
    elif m == 3:
        if d <= 20: print(a[11])
        else: print(a[0])
    elif m == 4:
        if d <= 19: print(a[0])
        else: print(a[1])
    elif m == 5:
        if d <= 20: print(a[1])
        else: print(a[2])
    elif m == 6:
        if d <= 20: print(a[2])
        else: print(a[3])
    elif m == 7:
        if d <= 22: print(a[3])
        else: print(a[4])
    elif m == 8:
        if d <= 22: print(a[4])
        else: print(a[5])
    elif m == 9:
        if d <= 22: print(a[5])
        else: print(a[6])
    elif m == 10:
        if d <= 22: print(a[6])
        else: print(a[7])
    elif m ==11:
        if d <= 22: print(a[7])
        else: print(a[8])
    elif m == 12:
        if d <= 21: print(a[8])
        else: print(a[9])