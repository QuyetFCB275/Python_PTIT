class person:
    def __init__(self, s : str, phone, date):
        a = s.split()
        self.ten = a[-1]
        self.ho_dem = " ".join(a[:-1])        
        self.phone = phone
        self.date = date
        
    def toString(self):
        return f'{self.ho_dem} {self.ten}: {self.phone} {self.date}'
    
f = open("SOTAY.txt", 'r')
s = f.read().split('\n')
a = []
for x in s:
    if len(x) > 0:
        a.append(x)
lit = []
i=0
day = ""
while i < len(a):
    if "/" in a[i]:
        day = a[i].split()[1]
        i += 1
    else:
        lit.append(person(a[i], a[i+1], day))
        i += 2
        

lit.sort(key=lambda x : (x.ten, x.ho_dem))
for x in lit:
    print(x.toString())