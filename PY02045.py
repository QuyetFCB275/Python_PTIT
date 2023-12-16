s = input()
while len(s) > 1:
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    c = int(a) + int(b)
    print(c)
    s = str(c)