from datetime import datetime
from math import*

class Player:
    def __init__(self, id, name, add, vt, time) -> None:
        self.id = id
        self.name = name
        self.add = add
        self.vt = vt
        self.time = time
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.add} {self.vt} Km/h'
    

if __name__ == '__main__':
    a = []
    t0 = datetime(year=1, month=1, day=1, hour=6)
    for i in range(int(input())):
        name, add, time = input(), input(), input()
        id = ''
        for x in add.split():
            id += x[0]
        for x in name.split():
            id += x[0]
            
        k = time.index(':')
        t1 = datetime(year=1, month=1, day=1, hour=int(time[0:k]), minute=int(time[k+1:]))
        sum_time = (t1 - t0).seconds / 3600
        vt = round(120 / sum_time)
        a.append(Player(id, name, add, vt, sum_time))
    a.sort(key=lambda x : x.time)
    for x in a:
        print(x)