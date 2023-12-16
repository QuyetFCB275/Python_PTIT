for i in range(int(input())):
    s = input()
    c = s[0]
    sum = 1
    for x in s[1:]:
        if x == c:
            sum += 1
        else:
            print(sum, c, sep='', end='')
            c = x
            sum = 1
    print(sum, c, sep='')