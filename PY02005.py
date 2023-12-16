def merge(a, l, m, r):
    b = a[l:m+1]
    c = a[m+1:r+1]
    n1, n2 = m - l + 1, r - m
    i, j, k = 0, 0, l
    sum = 0
    while i < n1 and j < n2:
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
            k += 1
        else:
            sum += n1 - i
            a[k] = c[j]
            j += 1
            k += 1
    while i < n1:
        a[k] = b[i]
        i += 1
        k += 1
    while j < n2:
        a[k] = c[j]
        j += 1
        k += 1
    return sum
    

def merge_sort(a = list, l = int(), r = int()):
    ans = 0
    if (l < r):
        m = (l + r) // 2
        ans += merge_sort(a, l, m)
        ans += merge_sort(a, m+1, r)
        ans += merge(a, l, m, r)
    return ans

if __name__ == '__main__':
    a = []
    n = int(input())
    a = list(map(int, input().split()))
    ans = merge_sort(a, 0, n-1)
    print(ans)