class SinhVien:
    def __init__(self, id, name, love):
        self.id = id
        self.name = name
        self.love = love
        self.d = 10
        
    def solve(self, tt):
        for i in tt:
            if i == 'm':
                self.d -= 1
            elif i == 'v':
                self.d -= 2
        if self.d < 0:
            self.d = 0
            
    def __str__(self):
        s = f'{self.id} {self.name} {self.love} {self.d}'
        if self.d == 0:
            s += ' ' + "KDDK"
        return s
    
if __name__ == "__main__":
    a = []
    m = {}
    n = int(input())
    for i in range(n):
        sv = SinhVien(input(), input(), input())
        m[sv.id] = sv
        a.append(sv)
        
    for i in range(n):
        id, tt = input().split()
        m[id].solve(tt)
        
    for x in a:
        print(x)