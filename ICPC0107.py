n = int(input())

def cv(a, b, p, q):
    a = a.replace(p, q)
    b = b.replace(p, q)
    return int(a) + int(b)

for i in range(n):
    p, q = input().split()
    s = input().split()
    # a, b = '', ''
    if len(s) > 1:
        a, b = s[0], s[1]
    else:
        a = s[0]
        b = input()
    
    ans1 = cv(a, b, p, q)
    ans2 = cv(a, b, q, p)
    print(min(ans1, ans2), max(ans1, ans2))