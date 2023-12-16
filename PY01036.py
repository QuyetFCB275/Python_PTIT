for i in range(int(input())):
    sum, n = 0, int(input())
    if n % 2 == 0:
        for j in range(2, n+1, 2):
            sum += 1 / j
    else:
        for j in range(1, n+1, 2):
            sum += 1 / j
    print("%.6f" %sum)