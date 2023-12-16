a = {}
i = 0
n = int(input())

while i < n:
    s = input()
    i += 1
    a[s] = 0
    
    while i < n:
        x = input()
        i += 1
        if len(x) == 0:
            break
        else:
            a[s] += 1
            
for x in a.keys():
    print(x, a[x], sep=': ')