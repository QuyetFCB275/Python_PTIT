class Flim:
    def __init__(self, id, tl, date, name, sum):
        self.id = id
        self.name = name
        self.date = date
        self.sum = sum
        self.kind = a1[tl].name
        self.dateee = date[-4:] + date[3:5] + date[:2]
    def __str__(self) -> str:
        return f'{self.id} {self.kind} {self.date} {self.name} {self.sum}'
        
class kindFlim:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    a1 = {}
    for i in range(1, n+1):
        id = "TL" + format(i, '03d')
        x = kindFlim(id, input())
        a.append(x)
        a1[id] = x
    b = []
    for i in range(1, m+1):
        id = 'P' + format(i, '03d')
        b.append(Flim(id, input(), input(), input(), int(input())))
    b.sort(key=lambda x : (x.dateee, x.name, -x.sum))
    for x in b:
        print(x)