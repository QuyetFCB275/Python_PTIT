ans = 1
n = int(input())
a = sorted(list(map(int, input().split())))
for x in a:
    if ans == x:
        ans += 1
print(ans)