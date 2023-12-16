a = [1] * 1000005
a[1] = 0
for i in range(2, 1000005):
    if a[i]:
        for j in range(i*2, 1000005, i):
            a[j] = 0

for i in range(int(input())):
    n = int(input())
    ans = 0
    for j in range(3, n - 5, 2):
        if a[j] == 1 and a[j+6] == 1 and (a[j+2] == 1 or a[j+4] == 1):
            ans += 1
    print(ans)