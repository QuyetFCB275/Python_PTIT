for i in range(int(input())):
    n, m, p = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = []
    i, j, k = 0, 0, 0
    while i < n and j < m and k < p:
        if a[i] == b[j] and b[j] == c[k]:
            ans.append(a[i])
            i+=1
            j+=1
            k+=1
        elif a[i] < b[j]:
            i+=1
        elif b[j] < c[k]:
            j+=1
        elif c[k] < a[i]:
            k+=1
    print("NO" if len(ans) == 0 else " ".join(map(str, ans)))