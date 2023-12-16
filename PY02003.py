# So good
a = [0]
for i in range(60):
    for j in range(40):
        for k in range(27):
            a.append(2**i * 3**j * 5**k)
a.sort()

def binary_search(l, r, val):
    while l <= r:
        idx = (l + r) // 2
        if a[idx] == val:
            return idx
        elif a[idx] < val:
            l = idx + 1
        else:
            r = idx - 1
    return -1

for t in range(int(input())):
    n = int(input())
    idx = binary_search(0, len(a) - 1, n)
    if idx == -1:
        print("Not in sequence")
    else:
        print(idx)