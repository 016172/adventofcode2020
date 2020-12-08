lin = []
acc = 0
switch = False
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
    print(instr,v)
    if not executed[i]:
        if instr == "acc":
            executed[i] = True
            i += 1
            acc += int(v)
        elif instr == "jmp":
            executed[i] = True
            if "jmp" in [i[:3] for i in lin[i+int(v):i-1]]:
                if not switch:
                    lin[i] = "nop " + str(v)
                    switch = True
                    i += 1
                else:
                    i += int(v)
        elif instr == "nop":
            print("här1")
            executed[i] = True

            if not switch:
                print("wooo")
                after = [i[:3] for i in lin[i+1:]]
                print(after)
                if "jmp" in after:
                    print("här2")
                    nv = after.index("jmp")
                    print(str(lin[nv+1]) + " wooo23123")
                    if executed[int(lin[nv+1].split(" ")[1])+i]:
                        lin[i] = "jmp " + str(2)
                        i += 2
                        switch = True
                    else:
                        print("här3")
                        i += 1
                        print(i)
            else:
                print("wtf")
                i += int(v)
        else:
            print("här")
            executed[i] = True
            i += 1
    else:
        break
print(acc)



#print(lin)
