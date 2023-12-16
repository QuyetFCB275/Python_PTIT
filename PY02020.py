n = int(input())
a = list(map(float, input().split()))
x, y = min(a), max(a)
b = [v for v in a if v != x and v != y]
print('%.2f' % (sum(b) / len(b)))