s = input()
ans = []
x = ""
for i in s:
    x += i
    if len(x) == 2:
        if int(x) not in ans:
            ans.append(int(x))
        x = ""
print(*ans)