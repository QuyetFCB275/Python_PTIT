def check(x):
    for i in x:
        if int(i) % 2 != 0:
            return False
    return True

a = []
x = 2
while x <= 888:
    s = str(x)
    if check(s):
        a.append(int(s + s[::-1]))
    x += 1

for i in range(int(input())):
    n = int(input())
    for x in a:
        if x < n:
            print(x, end=' ')
        else:
            break
    print()