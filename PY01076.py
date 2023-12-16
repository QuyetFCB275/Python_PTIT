def ucln(a, b):
    if b != 0:
        return ucln(b, a % b)
    return a

for i in range(int(input())):
    a = int(input())
    b = int(input())
    print(ucln(a, b))