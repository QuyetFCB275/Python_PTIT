n = int(input())
a = list(map(int, input().split()))
ans = []

for i in a:
    if len(ans) == 0 or (ans[-1] + i) % 2 != 0:
        ans.append(i)
    else:
        ans.pop(-1)
        
print(len(ans))        