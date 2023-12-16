for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(n):
        a.append([int(x) for x in input().split()])
    a.sort(key=lambda x : x[1])
    ans = 0
    end = 0
    for x in a:
        if x[0] >= end:
            ans += 1
            end = x[1]
    print(ans)