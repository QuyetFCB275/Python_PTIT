import re

a = []

while True:
    try:
        a.append(input().lower())
    except:
        break

for x in a:
    b = x.split()
    s = ""
    for x in b:
        if x == '.' or x == '!' or x == '?':
            s = s[0:-1] + x
            print(s[0].upper() + s[1:])
            s = ""
        else:
            s += x + " "
            if s[-2] in ('?', '!', '.'):
                print(s[0].upper() + s[1:])
                s = ""
    if len(s) > 0:
        print(s[0].upper() + s[1:-1] + ".")