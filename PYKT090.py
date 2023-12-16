a = set()

with open('VANBAN.in', 'r') as file:
    for line in file:
        a.add(line.strip().lower())
a = list(a)
a.sort()
print("\n".join(a))