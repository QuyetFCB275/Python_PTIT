s = input()
s = s[::-1]
a = str()
for i in range(len(s)):
    a += str(s[i])
    if (i + 1) % 3 == 0:
        a +=","
if a[-1] == ',':
    a = a[:-1]
print(a[::-1])