ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(int(line.replace("\n",  "")))
nbrvalid = 0
ins.sort()
f=[0]*len(ins)
f[0],f[1],f[2] = 1,1,2
for i in ins:


#0-0 1
#0-1, 1
#0-2, 1+1=2
#0-3, 1+1+1+1=4
#0-4 7
#0-6, 11
