for i in range(int(input())):
    a = input().split()
    ans = ''
    for x in a:
        if len(ans + x) <= 100:
            ans += x + " "
        else:
            break
    print(ans)