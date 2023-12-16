for i in range(int(input())):
    n = int(input())
    ans = 0
    a = list(map(int, input().split()))
    a.sort()
    for j in range(n-2):
        l, r = j + 1, len(a) - 1
        x = a[j]
        while l < r:
            if x + a[l] + a[r] == 0:
                ans += 1
                l += 1
            elif x + a[l] + a[r] > 0:
                r -= 1
            else: l += 1
    print(ans)