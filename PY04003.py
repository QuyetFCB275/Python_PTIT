from math import gcd

class PhanSo:
    def __init__(self, t, m):
        self.t = t
        self.m = m
    def rutgon(self):
        x = gcd(self.t, self.m)
        self.t //= x
        self.m //= x

a, b = map(int, input().split())
ps = PhanSo(a, b)
ps.rutgon()
print(ps.t, "/", ps.m, sep='')