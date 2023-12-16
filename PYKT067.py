a, ans = [], []
n = 0
count = 0

def Try(i:int, s:str):
    if i == n+1:
        ans.append(s)
        global count
        count += 1
        return
    for j in range(1, n+1):
        if a[j] == 0:
            a[j] = 1
            Try(i+1, s + str(j))
            a[j] = 0

for i in range(int(input())):
    n = int(input())
    ans.clear()
    a = [0] * 20
    count=0
    Try(1, "")
    ans.reverse()
    print(count, ' '.join(ans), sep='\n')