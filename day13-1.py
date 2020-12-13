ins,waittime = [],[]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
time,busses = int(ins[:1][0]),[int(_) for _ in ins[1:][0].split(',') if _ != "x"]
for i in busses:
    minWait = 0
    while((time+minWait)%i != 0):
        minWait += 1
    waittime.append((i,minWait))
z = min(waittime, key = lambda y: y[1])
print(z[0]*z[1])
