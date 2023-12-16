n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 1

a.sort()
for i in range(1, len(a)):
    if a[i]- a[i-1] > k:
        sum += 1
print(sum)