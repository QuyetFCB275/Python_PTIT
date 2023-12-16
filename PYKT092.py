dt = {1 : 1.5, 2 : 1, 3 : 0}

class thisinh:
    def __init__(self, id, name, sum):
        self.id = "TS" + format(id, '02d')
        self.name = name
        self.sum = sum
        self.status = ""
        if sum >= 20.5:
            self.status = "Do"
        else:
            self.status = "Truot"
        
    def __str__(self):
        return f'{self.id} {self.name} {self.sum} {self.status}'
    
if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        s = input().split()
        name = ' '.join(x.title() for x in s)
        
        diem = float(input())
        add = input()
        diemc = dt[int (input())]
        sum = diem + diemc
        if add != "Kinh":
            sum += 1.5
            
        a.append(thisinh(i+1, name, sum))
    a.sort(key=lambda x : -x.sum)
    for x in a:
        print(x)