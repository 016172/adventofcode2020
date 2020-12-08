lin = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        lin.append(line.replace("\n",  ""))
def ite():
    executed = [False]*len(lin)
    acc = 0
    i = 0
    while i < len(lin):
        h = lin[i].split(" ")
        instr,v = h[0],h[1]
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
            return None
    return acc
for j in range(0,len(lin)):
    st = lin[j].split(" ")
    instr, v = st[0],st[1]
    if instr == "nop":
        lin[j] = "jmp " + v
        test = ite()
        if test == None:
            lin[j] = instr + " " + v
        else:
            print(test)
            break
    elif instr == "jmp":
        lin[j] = "nop " + str(v)
        test = ite()
        if test == None:
            lin[j] = instr + " " + v
        else:
            print(test)
            break
