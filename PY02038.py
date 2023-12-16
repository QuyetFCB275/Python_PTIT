from math import factorial

n, ans = int(input()), 0
a = []
for i in range(n):
    s = input()
    z = [x for x in s]
    a.append(z)
b = []
for i in range(n):
    b.append([])

for x in a:
    k = x.count('C')
    if k > 1:
        ans += factorial(k) // (factorial(k-2) * 2)
    for i in range(len(x)):
        b[i].append(x[i])
for x in b:
    k = x.count('C')
    if k > 1:
        ans += factorial(k) // (factorial(k-2) * 2)
print(ans)