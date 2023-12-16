class Team:
    def __init__(self, id, name, sch) -> None:
        self.id = id
        self.name = name
        self.sch = sch
class Student:
    def __init__(self, id, name, name_team, sch) -> None:
        self.id = "C" + format(id, '03d')
        self.name = name
        self.name_team = name_team
        self.sch = sch
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.name_team} {self.sch}'

if __name__ == "__main__":
    n = int(input())
    dt = {}
    for i in range(n):
        id = "Team" + format(i + 1, '02d')
        name, sch = input(), input()
        dt[id] = Team(id, name, sch)
        
    a = []
    n = int(input())
    for i in range(n):
        name = input()
        id_team = input()
        a.append(Student(i+1, name, dt[id_team].name, dt[id_team].sch))
    a.sort(key=lambda x : x.name)
    for x in a:
        print(x)