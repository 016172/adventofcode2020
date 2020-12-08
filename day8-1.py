lin = []
acc = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        lin.append(line.replace("\n",  ""))
executed = [False]*len(lin)
i = 0
while i < len(lin):
    st = lin[i].split(" ")
    instr, v = st[0],int(st[1])
    if not executed[i]:
        if instr == "acc":
            executed[i] = True
            i += 1
            acc += int(v)
        elif instr == "jmp":
            executed[i] = True
            i = i + int(v)
        else:
            executed[i] = True
            i += 1
    else:
        break
print(acc)



#print(lin)
