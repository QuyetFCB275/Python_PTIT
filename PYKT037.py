n = int(input())

for i in range(0, n):
    sum, b = map(int, input().split())
    a = []
    while sum:
        a.append(sum % b)
        sum //= b
    s = ''.join(chr(x + 55) if x >= 10 else str(x) for x in reversed(a))
    print(s)