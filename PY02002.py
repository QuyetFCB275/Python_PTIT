f = [0] * 100
f[1] = f[2] = 1
for i in range(3, 100):
    f[i] = f[i-2] + f[i-1]
    
for i in range(int(input())):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        print(f[j], end=' ')
    print()