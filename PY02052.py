n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
sum1, sum2 = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            sum2 += a[i][j]
        elif i > j:
            sum1 += a[i][j]
print("YES" if abs(sum1-sum2) < int(input()) else "NO", abs(sum1-sum2), sep='\n')