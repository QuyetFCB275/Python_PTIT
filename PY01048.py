from math import *

for i in range(int(input())):
    n = int(input())
    ans = 0
    for j in range(2, isqrt(2*n)+1):
        if (j % 2 == 0 and n / j == n//j + 0.5) or (j % 2 == 1 and n % j == 0):
            k = n / j
            if j / 2 <= k:
                ans += 1
    print(ans)

"""
 Hướng giải quyết:
 Phân tích n ra một dãy các số tự nhiên liên tiếp (giả sử N số). Khi đó n = N * value_TB
 N sẽ là chẵn hoặc lẻ. Nếu N chẵn thì value_TB sẽ là lẻ 0.5, nếu N lẻ thì n % N == 0
"""
