a = set(input().lower().split())
b = set(input().lower().split())

ans1 = sorted(a.union(b))
ans2 = sorted(a.intersection(b))

print(type(ans1))
print(*ans1)
print(*ans2)