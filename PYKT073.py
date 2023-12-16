k, v = 0, 0
van = []
for i in range(int(input())):
    a = list(map(str, input().split()))
    if (len(a) == 6 or len(a) == 8):
        if k == 0:
            van.append(1)
        k += 1
    else:
        if v == 0:
            van.append(2)
            k = 0
        v = (v + 1) % 4

print(len(van))
for x in van:
    print(x)    