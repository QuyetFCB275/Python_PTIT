class matrix:
    def __init__(self, a, n, m) -> None:
        self.a = a
        self.n = n
        self.m = m
        
    def multiple(self):
        result = []
        for i in range(n):
            b = []
            for j in range(n):
                sum = 0
                for k in range(m):
                    sum += self.a[i][k] * self.a[j][k]
                b.append(sum)
            result.append(b)
        self.a = result
        
    def toString(self) -> str:
        for x in self.a:
            print(*x)
        
if __name__ == "__main__":
    for i in range(int(input())):
        v = []
        while len(v) < 2:
            v.extend(list(map(int, input().split())))
        n, m = v[0], v[1]
        v.pop(0)
        v.pop(0)
        a = []
        while len(v) != n*m:
            v.extend(list(map(int, input().split())))

        for i in range(n):
            a.append(v[n*i: n*i+5])
            
        ma_tran = matrix(a, n, m)
        ma_tran.multiple()
        ma_tran.toString()