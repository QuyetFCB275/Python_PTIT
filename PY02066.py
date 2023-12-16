n = int(input())
a = []
while len(a) < n:
    a.extend([int(x) for x in input().split()])
if n == a[-1]:
    print("Excellent!")
else:
    for i in range(1, a[-1]):
        if i not in a:
            print(i)