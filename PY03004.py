def check(s):
    for x in s:
        if not x.isalnum():
            return False
    return True

a = {}
for i in range(int(input())):
    b = input().lower().split()
    separator = ['.', ',', '/', '?', '!', ':', ';', '-', '(', ')']
    for sep in separator:
        b = [item for x in b for item in x.split(sep)]
    for x in b:
        if len(x) > 0 and check(x):
            if x in a:
                a[x] += 1
            else:
                a[x] = 1
c = []
for items in a.items():
    c.append(items)
c.sort(key=lambda x : (-x[1], x[0]))
for x in c:
    print(x[0], x[1])

# Solution2:
'''
import re

a = []
dt = {}

def check(s: str):
    for x in s:
        if not x.isalnum():
            return False
    return True


for i in range(int(input())):
    text = input().strip().lower()
    b = re.split('[ ,.?!:;)(-/]', text)
    for x in b:
        if len(x) > 0 and check(x):
            if x in dt:
                dt[x] += 1
            else:
                dt[x] = 1

for x in dt.items():
    a.append(x)
a.sort(key=lambda x: (-x[1], x[0]))
for x in a:
    print(x[0], x[1])
'''
