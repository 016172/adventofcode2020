ins = []
dirs = {"N":0,"E":0,"S":0,"W":0,"dir":"E"}
deg = [0,90,180,270,360]
totdegree = 0
di = ["E","S","W","N"]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
for i in ins:
    instr,v = i[:1],int(i[1:])
    if instr == "F":
        dirs[dirs["dir"]] = dirs[dirs["dir"]] + v
    elif instr == "R":
        totdegree = (totdegree + v)%360
        dirs["dir"] = di[deg.index(totdegree)]
    elif instr == "L":
        totdegree = (totdegree - v)%360
        dirs["dir"] = di[deg.index(totdegree)]
    else:
        dirs[instr] = dirs[instr] + v
print(abs(dirs["N"]-dirs["S"]) + abs(dirs["E"]-dirs["W"]))





    #1
#2     #3
    #4
