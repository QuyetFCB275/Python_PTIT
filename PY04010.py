class person:
    def __init__(self, name, date, sum) -> None:
        self.name = name
        self.date = date
        self.sum = sum
        
    def __str__(self) -> str:
        return f'{self.name} {self.date} {self.sum:.1f}'
    
a = person(input(), input(), (float(input()) + float(input()) + float(input())))
print(a)