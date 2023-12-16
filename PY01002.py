s = input()
a = []
for x in s:
    if x.isdigit():
        a.append(int(x))
x, y, z = a
if x + y == z:
    print("YES")
else: print("NO")