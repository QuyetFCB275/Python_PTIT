class Complex:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def add(self, b):
        return Complex(self.x + b.x, self.y + b.y)
    def mul(self, b):
        return Complex(self.x * b.x - self.y * b.y, self.x * b.y + self.y * b.x)
    def __str__(self) -> str:
        return f'{self.x} {"-" if self.y < 0 else "+"} {abs(self.y)}i'
    
for i in range(int(input())):
    a = [int(x) for x in input().split()]
    x1 = Complex(a[0], a[1])
    x2 = Complex(a[2], a[3])
    print(x1.add(x2).mul(x1), (x1.add(x2)).mul(x1.add(x2)), sep=', ')