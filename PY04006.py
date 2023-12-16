from math import*

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, b):
        return sqrt(pow(self.x - b.x, 2) + pow(self.y - b.y, 2))
    
class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def solve(self):
        a = self.x.distance(self.y)
        b = self.y.distance(self.z)
        c = self.z.distance(self.x)
        if a + b <= c or b + c <= a or a + c <= b:
            return "INVALID"
        return '{:.2f}'.format(sqrt((a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c)) / 4)
    
zan = []
n = int(input())
for i in range(n):
    zan += [float(i) for i in input().split()]
    tg = Triangle(Point(zan[6*i], zan[6*i+1]), Point(zan[6*i + 2], zan[6*i+3]), Point(zan[6*i + 4], zan[6*i+5]))
    print(tg.solve())