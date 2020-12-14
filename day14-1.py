ins,vmask,stored,sum = [],0,dict(),0
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
for i in range(len(ins)):
    z = ins[i].split(" = ")
    if z[0] == "mask":
        vmask = z[1]
    else:
        loc,val = int(z[0].split("[")[1].replace("]","")),list(bin(int(z[1])).split('b')[1])
        for i in range(len(vmask)-len(val),0,-1):
            val.insert(0,'0')
        for i in range(len(vmask)):
            if val[i] != vmask[i] and vmask[i] != 'X':
                val[i] = vmask[i]
        stored[loc] = ''.join(val)
for i in stored.values():
    sum+=int(i,2)
print(sum)
