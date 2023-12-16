n = input()
f = [0] * 15 # Kiểm tra xem ký tự thứ i trong sâu s được use chưa

def Try(s):
    if len(s) == len(n):
        print(s)
        return
    for i in range(len(n)):
        if f[i] == 0:
            f[i] = 1
            Try(s + n[i])
            f[i] = 0

Try('')