for i in range(int(input())):
    n = input()
    a = [int(x) for x in input().split()]
    ans = []
    for x in a:
        if x in ans:
            ans.remove(x)
        else:
            ans.append(x)
    print(*ans)