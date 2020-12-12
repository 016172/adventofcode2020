ins = []
dirs = {"N":0,"E":0,"S":0,"W":0,"dir":"E"}
waypoint = [10,0,0,1]
di = ["E","S","W","N"]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
for i in ins:
    instr,v = i[:1],int(i[1:])
    if instr == "F":
        newPos = [i*v for i in waypoint]
        for i in range(len(newPos)):
            dirs[di[i]] += newPos[i]
    elif instr == "R":
        if v == 90:
            waypoint = [waypoint[3],waypoint[0],waypoint[1],waypoint[2]]
        elif v == 180:
            waypoint = [waypoint[2],waypoint[3],waypoint[0],waypoint[1]]
        elif v == 270:
            waypoint = [waypoint[1],waypoint[2],waypoint[3],waypoint[0]]
    elif instr == "L":
        if v == 90:
            waypoint = [waypoint[1],waypoint[2],waypoint[3],waypoint[0]]
        elif v == 180:
            waypoint = [waypoint[2],waypoint[3],waypoint[0],waypoint[1]]
        elif v == 270:
            waypoint = [waypoint[3],waypoint[0],waypoint[1],waypoint[2]]
    else:
        waypoint[di.index(instr)] += v
print(abs(dirs["N"]-dirs["S"]) + abs(dirs["E"]-dirs["W"]))
