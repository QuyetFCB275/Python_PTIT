from math import*

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, b):
        return sqrt(pow(self.x - b.x, 2) + pow(self.y - b.y, 2))
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ab = a.distance(b)
        self.bc = b.distance(c)
        self.ca = c.distance(a)
    def chuvi(self):
        if self.ab + self.bc <= self.ca or self.bc + self.ca <= self.ab or self.ca + self.ab <= self.bc:
            return 'INVALID'
        return "{:.3f}".format(self.ab + self.bc + self.ca)

inp = []
t = int(input())
for case in range(t):
    inp += [float(i) for i in input().split()]
i = 0
for case in range(t):
    triangle = Triangle(Point(inp[i], inp[i + 1]), Point(inp[i + 2], inp[i + 3]), Point(inp[i + 4], inp[i + 5]))
    print(triangle.chuvi())
    i += 6