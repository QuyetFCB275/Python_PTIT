import re

ans = []
for i in range(int(input())):
    s = input().lower()
    a = re.split('[a-z]', s)
    ans.extend([int(x) for x in a if x.isdigit()])
ans.sort()
for x in ans:
    print(x)