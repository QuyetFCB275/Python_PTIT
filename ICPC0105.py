n = int(input())

for i in range(0, n):
    s = input()
    ans, sum = 0, 0
    for x in s:
        if x.isdigit():
            sum = sum * 10 + int(x)
        else:
            ans = max(ans, sum)
            sum = 0
    print(max(ans, sum))