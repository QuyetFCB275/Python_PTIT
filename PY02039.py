n = int(input())
ans1, ans2 = 0, 0
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if j > i:
            ans1 += a[j]
        elif j < i:
            ans2 += a[j]
k = int(input())
if abs(ans1 - ans2) <= k :
    print("YES")
else:
    print("NO")
print(abs(ans1 - ans2))