import re

s = ''

while True:
    try:
        s += input()
    except EOFError:
        break

a = re.split('[.?!]', s)

def check(x : str):
    if len(x) > 0:
        for i in x:
            if i.isalnum():
                return True
    return False

for i in a:
	if len(i) > 0:
		x = i.lower().split()
		x[0] = x[0].title()
		ans = " ".join(x)
		if check(ans):
			print(ans)