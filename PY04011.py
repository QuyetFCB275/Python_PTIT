dt = {}
a = []
se = set()
mp_in = {}
que = []
cnt = 0

def kahn():
    while len(que) > 0:
        global cnt

        u = que[0]
        cnt += 1
        que.pop(0)
        for v in dt[u]:
            mp_in[v] -= 1
            if mp_in[v] == 0:
                que.append(v)


if __name__ == "__main__":
    n = int(input())
    while True:
        try:
            a.extend(input().split())
        except:
            break

    for i in range(n):
        se.add(a[3 * i])
        se.add(a[3 * i + 2])

    for x in se:
        dt[x] = []
        mp_in[x] = 0

    for i in range(n):
        if a[3 * i + 1] == '>':
            dt[a[3 * i]].append(a[3 * i + 2])
            mp_in[a[3 * i + 2]] += 1
        else:
            dt[a[3 * i + 2]].append(a[3 * i])
            mp_in[a[3 * i]] += 1

    for x in se:
        if mp_in[x] == 0:
            que.append(x)


    kahn()
    if cnt == n:
        print("possible")
    else:
        print("impossible")