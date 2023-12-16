for i in range(int(input())):
    n = input()
    a = [int (x) for x in n]
    summ = sum(a)
    s = str(summ)
    if len(s) > 1 and s == s[::-1]:
        print("YES")
    else:
        print("NO")