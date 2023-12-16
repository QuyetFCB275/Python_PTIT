for i in range(int(input())):
    n = input()
    ans = 1
    for x in n:
        if x > '0':
            ans *= int(x)
    print(ans)