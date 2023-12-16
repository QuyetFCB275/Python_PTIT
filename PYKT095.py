dt = {'A':100, 'B':500, 'C':200}

class Customer:
    def __init__(self, id, name, kind, count) -> None:
        self.id = "KH" + format(id, '02d')
        self.name = name
        self.kind = kind
        self.count = count
    def money_in(self):
        x = dt[self.kind]
        return self.count * 450 if self.count < x else x * 450
    def money_out(self):
        x = dt[self.kind]
        return (self.count - x) * 1000 if self.count > x else 0
    def money_vat(self):
        return self.money_out() // 20
    def money_sum(self):
        return self.money_in() + self.money_out() + self.money_vat()
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.money_in()} {self.money_out()} {self.money_vat()} {self.money_sum()}'
    
if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        name = input().split()
        name = ' '.join(x.title() for x in name)
        s = input().split()
        kind = s[0]
        count = int(s[2]) - int(s[1])
        a.append(Customer(i+1, name, kind, count))
    a.sort(key=lambda x : -x.money_sum())
    for x in a:
        print(x)