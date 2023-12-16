def solve(minn, maxx):
    i=1
    while minn * 2**(i+1) < maxx:
        i+=1
    return i

for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n-1):
        maxx = max(a[i], a[i+1])
        minn = min(a[i], a[i+1])
        if maxx <= 2*minn:
            continue
        ans += solve(minn, maxx)
    print(ans)