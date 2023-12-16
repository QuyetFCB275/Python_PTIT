ans = []
n = 0

def Try(i:int, sum:int, s:str):
    if sum > n:
        return
    if sum == n:
        s = s[0:-1]
        ans.append(s)
        return
    for j in range(i, 0, -1):
        Try(j, sum+j, s + str(j) + " ")
        
if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        Try(n, 0, "")
        print(len(ans))
        for i in ans:
            print("(" + i + ")", end=' ')
        ans.clear()
        print()