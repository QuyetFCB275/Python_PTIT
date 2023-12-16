def check(s):
    if len(s) % 2 == 0 or s[0] == s[1] or s[0] != s[-1]:
        return False
    for i in range(len(s)):
        if s[i] != s[0] and i % 2 == 0:
            return False
    return True

for i in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")