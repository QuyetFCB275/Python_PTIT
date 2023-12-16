dt = {}
a = []

class Exam:
    def __init__(self, id, id_m, name, date, time, gr) -> None:
        self.id = "T" + format(id, '03d')
        self.id_m = id_m
        self.name = name
        self.date = date
        self.time = time
        self.gr = gr
        
        self.day = date[6:] + date[3:5] + date[0:2]
    def __str__(self) -> str:
        return f'{self.id} {self.id_m} {self.name} {self.date} {self.time} {self.gr}'

if __name__ == "__main__":
    n, m = map(int, input().split())
    for i in range(n):
        id, name = input(), input()
        dt[id] = name
    for i in range(m):
        s = input().split()
        id_m = s[0]
        date = s[1]
        time = s[2]
        gr = s[3]
        name = dt[id_m]
        a.append(Exam(i+1, id_m, name, date, time, gr))
    a.sort(key=lambda x : (x.day, x.time, x.id_m))
    
    for x in a:
        print(x)  