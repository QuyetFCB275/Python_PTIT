for i in range(int(input())):
    s = input()
    if s.count('0') + s.count('1') + s.count('2') == len(s):
        print("YES")
    else:
        print("NO")