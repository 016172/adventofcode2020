import math
k = []
c = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        c.append(line.replace("\n",""))
    else:
        b = []
        counter = 0
        v = dict()
        for i in c:
            counter += 1
            for j in i:
                b.append(j)
        for i in b:
            if not i in v.keys():
                v[i] = 1
            else:
                v[i] = v[i] + 1
        cv = 0
        for i in v.values():
            if i == counter:
                cv += 1
        if counter == 1:
            k.append(sum(v.values()))
        else:
            k.append(cv)
        c = []
total = 0
for i in k:
    total += i
print(math.ceil(total))
