for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    b = []
    for i in range(n):
        while len(b) > 0 and a[b[-1]] <= a[i]:
            b.pop(-1)
        if len(b) == 0:
            ans.append(i + 1)
        else:
            ans.append(i - b[-1])
        b.append(i)
    for x in ans:
        print(x, end=' ')
    print()