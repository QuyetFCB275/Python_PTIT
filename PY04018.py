dt = {1 : 2, 2 : 1.5, 3 : 1, 4 : 0}
sb = {"A" : "TOAN", "B" : "LY", "C" : "HOA"}

class GV:
    def __init__(self, id, name, sub, score, status):
        self.id = "GV" + format(id, '02d')
        self.name = name
        self.sub = sub
        self.score = score
        self.status = status
    
    def __str__(self):
        return f'{self.id} {self.name} {self.sub} {self.score:.1f} {self.status}'
    
if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        name = input()
        mon = input()
        sub = sb[mon[0]]
        k = dt[int (mon[1])]
        
        d1 = float(input())
        d2 = float(input())
        sum = d1 * 2 + d2 + k
        status = ""
        if sum >= 18:
            status = "TRUNG TUYEN"
        else:
            status = "LOAI"
        
        a.append(GV(i+1, name, sub, sum, status))
        
    a.sort(key=lambda x : -x.score)
    for x in a:
        print(x)