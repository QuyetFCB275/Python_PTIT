for i in range(int(input())):
    n = int(input())
    a, b, c = 10**10, 10**10, 10**10
    lit = list(map(int, input().split()))
    a = min(lit)
    lit.remove(a)
    b = min(lit)
    lit.remove(b)
    c = min(lit)
    print(a+b+c)