s = input()
l, u = 0, 0
for x in s:
    if x.islower():
        l += 1
    else: u += 1
if l < u:
    print(s.upper())
else:
    print(s.lower())