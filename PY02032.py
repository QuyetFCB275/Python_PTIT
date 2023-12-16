s = input()
ans = set()
x = ""
for i in s:
    x += i
    if len(x) == 2:
        ans.add(int(x))
        x = ""
ans = list(ans)
print(*sorted(ans))