import math
ins = []
calcs = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    ins.append(line.replace("\n",""))
for i in ins:
    print(i[:7])
    rows = [i for i in range(0,128)]
    columns = [i for i in range(0,8)]
    for j in i[:7]:
        if j == "F":
            rows = rows[:int(len(rows)/2)]
        else:
            rows = rows[int(len(rows)/2):]
    for k in i[7:]:
        if k == "R":
            columns = columns[int(len(columns)/2):]
        else:
            columns = columns[:int(len(columns)/2)]
    calcs.append(sum(rows)*8 + sum(columns))
calcs.sort()
possible = []
for i in calcs:
    for j in calcs:
        if i+1 == j-1:
            possible.append(i+1)
for i in calcs:
    if i in possible:
        possible.remove(i)
print(possible)
