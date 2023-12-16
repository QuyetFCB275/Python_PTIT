for i in range(int(input())):
    s = input()
    l = len(s) // 2
    a = s[:l]
    b = s[l:]
    sum1, sum2 = 0, 0
    for x in a:
        sum1 += ord(x) - 65
        sum1 %= 26
    for x in b:
        sum2 += ord(x) - 65
        sum2 %= 26
    s1 = ""
    for i in range(len(a)):
        s1 += chr((ord(a[i]) + sum1) % 90 + 64 if (ord(a[i]) + sum1) > 90 else (ord(a[i]) + sum1))
    s2 = ""
    for i in range(len(a)):
        s2 += chr((ord(b[i]) + sum2) % 90 + 64 if (ord(b[i]) + sum2) > 90 else (ord(b[i]) + sum2))
    ans = ""
    for i in range(len(s1)):
        ans += chr((ord(s1[i]) + ord(s2[i]) - 65) % 90 + 64 if (ord(s1[i]) + ord(s2[i]) - 65) > 90 else (ord(s1[i]) + ord(s2[i])) - 65)
    print(ans)