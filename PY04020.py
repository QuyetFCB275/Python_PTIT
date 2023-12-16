class bill:
    def __init__(self, id, name, count, cost, discount):
        self.id = id
        self.name = name
        self.count = count
        self.cost = cost
        self.discount = discount
        self.sum = self.cost * self.count - self.discount
    
    def __str__(self):
        return f'{self.id} {self.name} {self.count} {self.cost} {self.discount} {self.sum}'
    
if __name__ == "__main__" :
    a = []
    for i in range(int(input())):
        a.append(bill(input(), input(), int(input()), int(input()), int(input())))
    a.sort(key=lambda x : -x.sum)
    for x in a:
        print(x)