for i in range(int(input())):
    s, ans = input(), ""
    for i in range(len(s)):
        if  s[i].isalpha():
            ans += (s[i] * (int (s[i+1])))
    print(ans)