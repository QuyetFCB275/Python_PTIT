class sinhvien:
    def __init__(self, id, name, avg) -> None:
        self.id = "HS" + format(id, '02d')
        self.name = name
        self.avg = avg
        self.result = "XUAT SAC" if avg >= 9 else ("GIOI" if avg >= 8 else ("KHA" if avg >= 7 else ("TB" if avg >= 5 else "YEU")))
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.avg:.1f} {self.result}'
    
if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        s = input()
        b = list(map(float, input().split()))
        tong_diem = (b[0] + b[1]) * 2.0 + sum(b[2:]) 
        avg = round(tong_diem / 12 + 0.01, 1)
        # print(avg)
        a.append(sinhvien(i+1, s, avg))
    a.sort(key=lambda x : -x.avg)
    for x in a:
        print(x)
        