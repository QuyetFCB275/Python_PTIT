dt = {"A1" : 10, "A4" : 12, "A9" : 14, "A16" : 20,
      "B1" : 10, "B4" : 11, "B9" : 13, "B16" : 16,
      "C1" : 9, "C4" : 10, "C9" : 12, "C16" : 14,
      "D1" : 8, "D4" : 9, "D9" : 11, "D16" : 13}

class Staff:
    def __init__(self, id, name, dv, salary) -> None:
        self.id = id
        self.name = name
        self.dv = dv
        self.salary = salary
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.dv} {self.salary}'
    
if __name__ == "__main__":
    dic = {}
    a = []
    for i in range(int(input())):
        s = input()
        id_room = s[0:2]
        name = s[3:]
        dic[id_room] = name
    for i in range(int(input())):
        id, name, money, cnt = input(), input(), int(input()), int(input())
        year = int(id[1:3])
        k = id[0] + str(1 if year <= 3 else 4 if year <= 8 else 9 if year <= 15 else 16)
        x = dt[k]
        a.append(Staff(id, name, dic[id[3:]],money * cnt * x * 1000))
    for x in a:
        print(x)