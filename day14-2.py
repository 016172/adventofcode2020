from itertools import combinations
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
        tried = []
        sum = 0
        loc,val = int(z[0].split("[")[1].replace("]","")),list(bin(int(z[1])).split('b')[1])
        locs = list(bin(loc).split('b')[1])
        for i in range(len(vmask)-len(locs),0,-1):
            locs.insert(0,'0')
        for i in range(len(vmask)):
            if vmask[i] != '0':
                locs[i] = vmask[i]
        for k in combinations([0,1]*locs.count('X'),locs.count('X')):
            if list(k) not in tried:
                tried.append(list(k))
        indices = []
        for i in range(len(locs)):
            if locs[i] == 'X':
                indices.append(i)
        for i in tried:
            cntr = 0
            tmp = locs
            for j in indices:
                tmp[j] = i[cntr]
                cntr += 1
            stored[int(''.join(str(e) for e in tmp),2)] = ''.join(val)
for i in stored.values():
    sum += int(i,2)
print(sum)
