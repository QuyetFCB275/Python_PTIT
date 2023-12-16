d = {"000":0, "001":1, "010":2, "011":3, "100":4, "101":5, "110":6, "111":7}

s = input()[::-1]
ans = ""
tmp = ""
for i in range(len(s)):
    tmp = s[i] + tmp
    if (i + 1) % 3 == 0:
        ans = (str)(d[tmp]) + ans
        tmp = ""
if len(tmp) > 0:
    if len(tmp) == 1:
        tmp = "00" + tmp
    else:
        tmp = "0" + tmp
    ans = (str)(d[tmp]) + ans
print(ans)