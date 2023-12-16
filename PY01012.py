a = input()
b = input()
p = int(input()) - 1
ans = a[:p] + b + a[p:]
print(ans)