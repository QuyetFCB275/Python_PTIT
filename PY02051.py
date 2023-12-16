n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
ans = []
sum1, sum2 = 0, 0
for i in range(n):
    for j in range(n):
        if i == 0:
            sum1  += a[i][j]
        elif j > i:
            sum2 += a[i][j]
if n == 2:
    if sum1 % 2 == 0:
        ans.append(sum1//2)
        ans.append(sum1//2)
    else:
        ans.append(sum1//2)
        ans.append(sum1//2 + 1)
else:
    x = (sum1 - sum2//(n-2))//(n-1)
    ans.append(x)
    for i in range(1, n):
        ans.append(a[0][i] - x)
print(*ans)