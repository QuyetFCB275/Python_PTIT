from datetime import datetime

m = {1:25, 2:34, 3:50, 4:80}

class KH:
    def __init__(self, n, r, d1, d2, m, id):
        self.name = n
        self.room = r
        self.d1, self.d2 = d1, d2
        self.m = m
        self.id = "KH" + format(id, '02d')
        self.sum_day, self.sum_money = 0, 0
        
    def solve(self):
        delta = datetime.strptime(self.d2, "%d/%m/%Y") - datetime.strptime(self.d1, "%d/%m/%Y")
        self.sum_day = delta.days + 1
        self.sum_money = self.sum_day * m[int (self.room[0])] + int (self.m)
    
    def __str__(self):
        return f'{self.id} {self.name} {self.room} {self.sum_day} {self.sum_money}'
    
if __name__ == "__main__":
    a = []
    n = int(input())
    for i in range(n):
        x = KH(input().strip(), input().strip(), input().strip(), input().strip(), input(), i + 1)
        x.solve()
        a.append(x)
    a.sort(key= lambda x : (- x.sum_money))
    print(*a, sep='\n')