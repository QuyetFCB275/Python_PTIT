class Rectangle:
    def __init__(self, d, r, c):
        self.d, self.r, self.c = d, r, c
    
    def perimeter(self):
        return 2 * (self.d + self.r)
    def area(self):
        return self.d * self.r
    def color(self):
        return self.c.title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")