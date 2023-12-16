n = int(input())

while n:
    a = []
    while len(a) < n:
        a.append(int(input()))
    a.sort(reverse=False)
    
    if a[0] == a[-1]:
        print("BANG NHAU")
    else:
        print(a[0], a[-1])
    n = int(input())