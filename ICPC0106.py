n = int(input())

for i in range(0, n):
    b, s = int(input()), input()
    sum, k = 0, 0
    for x in s[::-1]:
        sum = sum + int(x) * (2 ** k)
        k += 1
    a = []
    while sum:
        a.append(sum % b)
        sum //= b
    s = ''.join(chr(x + 55) if x >= 10 else str(x) for x in reversed(a))
    print(s)