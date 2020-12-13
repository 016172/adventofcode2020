ins,waittime = [],[]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
busses = ins[0].split(',')
offset = []
for i in range(len(busses)):
    offset.append((busses[i],i))
offset = [(int(_[0]),_[1]) for _ in offset if _[0] != 'x']
t = 0
modcalc = offset[0][0]
print(offset)
while True:
    if all((t+y)%modcalc==y for (x,y) in offset):
        break
    else:
        t += 1
        print(t)

print(t)
