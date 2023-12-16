f = [1] * 1000005
for i in range(2, 1000005):
    if f[i]:
        for j in range(i*2, 1000005, i):
            f[j] = 0
            
for i in range(int(input())):            
    n = int(input())
    for a in range(13, n):
        b = str(a)
        b = ''.join(reversed(b))
        b = int(b)
        if f[a] and f[b] and a < b and b < n:
            print(a, b, end=' ')
    print()