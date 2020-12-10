ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(int(line.replace("\n",  "")))
ins.sort()
f=[0]*(max(ins)+1)
n = ins[2]
f[0],f[ins[0]],f[ins[1]] = 1,1,2
while n < max(ins)+1:
    if not n in ins:
        f[n] = 0
    else:
        f[n] = (f[n-1] + f[n-2] + f[n-3])
    n += 1
print(max(f))



#0-0 1
#0-1, 1
#0-2, 1+1=2
#0-3, 1+1+1+1=4
#0-4 7
#0-6, 11

#0-0 1
#0-1 1
#0-2 2
#0-3 4
#0-6 4
#0-9 4
#0-10 4
#0-11 8
#0-12 16
