for i in range(int(input())):
    a = [int(x) for x in input()]
    a = a[::-1]
    for i in range(1, len(a)):
        if a[i-1] >= 5:
            a[i] += 1
    s = str (a[-1]) + "".join(str(x) for x in ([0] * (len(a) - 1)))
    print(s)