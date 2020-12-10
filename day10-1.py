ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(int(line.replace("\n",  "")))
ins.sort()
x,y = 0,0
if ins[0] == 1:
    x += 1
elif ins[0] == 3:
    y += 1
for i in range(1,len(ins)):
    if ins[i] - ins[i-1] == 1:
        x += 1
    if ins[i] - ins[i-1] == 3:
        y += 1
print(x,y+1)
