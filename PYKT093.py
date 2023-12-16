from math import*

class Student:
    def __init__(self, id, name, score) -> None:
        self.id = "SV" + format(id, '02d')
        self.name = name
        self.score = score
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.score:.2f}'
    
if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        name = input().strip().lower().split()
        name = " ".join(x.title() for x in name)
        score = (int(input()) * 3 + int(input()) * 3 + int(input()) * 2) / 8 + 0.001
        a.append(Student(i+1, name, score))
    a.sort(key=lambda x : -x.score)
    maxx, k = a[0].score, 1
    for i in range(1, len(a)+1):
        q = a[i-1]
        if q.score != maxx:
            maxx = q.score
            k = i
        print(q, k)