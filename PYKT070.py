class monthi:
    def __init__(self, idm, name, kind):
        self.idm = idm
        self.name = name
        self.kind = kind
    def __str__(self):
        return f'{self.name}'

class cathi:
    def __init__(self, id, day, hour, idp):
        self.id = id
        self.day = day
        self.hour = hour
        self.idp = idp
    def __str__(self):
        return f'{self.day} {self.hour} {self.idp}'

class lichthi:
    def __init__(self, ca, mon, gr, count):
        self.ca = ca
        self.mon = mon
        self.gr = gr
        self.count = count
        self.day = ca.day
        self.hour = ca.hour

    def __str__(self):
        return f'{self.ca} {self.mon} {self.gr} {self.count}'

    def comp(self):
        s = self.day[6:] + self.day[3:5] + self.day[0:2] + self.hour
        return s

a, b, ans = {}, {}, []

with open('C:\\Users\\admin\\OneDrive\\Máy tính\\VanVan\\MONTHI.in', 'r') as file:
    n = int(next(file).strip())
    for i in range(n):
        idm, name, kind = next(file).strip(), next(file).strip(), next(file).strip()
        a[idm] = monthi(idm, name, kind)

with open('C:\\Users\\admin\\OneDrive\\Máy tính\\VanVan\\CATHI.in', 'r') as file:
    n = int(next(file).strip())
    for i in range(1, n+1):
        id, day, hour, idp = "C" + format(i, '03d'), next(file).strip(), next(file).strip(), next(file).strip()
        b[id] = cathi(id, day, hour, idp)

with open('C:\\Users\\admin\\OneDrive\\Máy tính\\VanVan\\LICHTHI.in', 'r') as file:
    file.readline()
    line = file.readline().split()
    while line:
       idc, idm, gr, count = line
       mon = a[idm]
       ca = b[idc]

       ans.append(lichthi(ca, mon, gr, count))
       line = file.readline().split()

ans.sort(key=lambda x : x.comp())
for x in ans:
    print(x)