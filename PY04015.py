from datetime import datetime

m = {1:25, 2:34, 3:50, 4:80}

class KH:
    def __init__(self, id, name, new, old):
        self.id = "KH" + format(id, '02d')
        self.name = name
        self.count = old - new
        self.sum = 0
        
    def solve(self):
        k = self.count
        if k <= 50:
            self.sum = 100 * k * 1.02
        elif k <= 100:
            self.sum = (100 * 50 + 150 * (k - 50)) * 1.03
        else:
            self.sum = (100 * 50 + 150 * 50 + 200 * (k - 100)) * 1.05 
        # self.sum = round(self.sum)
    
    def __str__(self):
        return f'{self.id} {self.name} {self.sum:.0f}'
    
if __name__ == "__main__":
    a = []
    n = int(input())
    for i in range(n):
        x = KH(i + 1, input(), int(input()), int(input()))
        x.solve()
        a.append(x)
    a.sort(key= lambda x : - x.sum)
    for x in a:
        print(x)