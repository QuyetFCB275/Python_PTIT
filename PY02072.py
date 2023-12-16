n = int(input())
a = [int(x) for x in input().split()] + [-1]
ans, dem, k = 0, 0, max(a)
for x in a:
    if x == k:
        dem += 1
    else:
        ans = max(ans, dem)
        dem = 0
print(ans)