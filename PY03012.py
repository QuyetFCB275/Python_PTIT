zan = []
n = int(input())
for i in range(n):
    s = input()
    a, b = map(int, input().split())
    zan.append((s, a, b))
zan.sort(key= lambda x : (-x[1], x[2], x[0]))
for x in zan:
    print(x[0], x[1], x[2])