ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
for i in range(26,len(ins)):
    found = False
    for j in range(0+(i-26),26+(i-26)):
        for z in range(0,j):
            if int(ins[j]) + int(ins[z]) == int(ins[i]):
                found = True
                break
    if not found:
        print(int(ins[i]))
        break
