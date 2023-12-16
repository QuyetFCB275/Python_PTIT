from math import *

class PhanSo:
    def __init__(self, t, m):
        self.t = t
        self.m = m
        
    def rutgon(self):
        x = gcd(self.t, self.m)
        self.t //= x
        self.m //= x
        
    def add(self, p2):
        k = self.m * p2.m // gcd(self.m, p2.m)
        self.t = int (self.t * k / self.m + p2.t * k / p2.m)
        self.m = k

a, b, c, d = map(int, input().split())
p1 = PhanSo(a, b)
p2 = PhanSo(c, d)
p1.add(p2)
p1.rutgon()
print(p1.t, "/", p1.m, sep='')