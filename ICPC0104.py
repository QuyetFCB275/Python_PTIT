if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        s = input()
        a = []
        sum = 0
        for x in s:
            if x.isdigit():
                sum = sum * 10 + int(x)
            elif sum > 0:
                a.append(sum)
                sum = 0
        if sum:
            a.append(sum)
        print(min(a))