k = []
c = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        c.append(line.replace("\n",""))
    else:
        b = set()
        for i in c:
            for j in i:
                b.add(j)
        k.append(b)
        c = []
total = 0
for i in k:
    total += len(i)
print(total)
