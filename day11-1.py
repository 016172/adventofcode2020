ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
height,length = len(ins),len(ins[0])
def findadj(i,j):
    nbr = 0
    if not ins[i][j] == ".":
        if i == 0 and (not j == 0 and not j+1 == length):
            for x in [i,i+1]:
                for y in [j-1,j+1]:
                    if ins[x][y] == "#":
                        nbr += 1
            if ins[i+1][j] == "#":
                nbr += 1
        elif 1 <= i <= height-2 and j == 0:
            for x in [i-1,i+1]:
                for y in [j,j+1]:
                    if ins[x][y] == "#":
                        nbr += 1
            if ins[i][j+1] == "#":
                nbr += 1
        elif i+1 == height and (not j == 0 and not j+1 == length):
            for x in [i-1,i]:
                for y in [j-1,j+1]:
                    if ins[x][y] == "#":
                        nbr += 1
            if ins[i-1][j] == "#":
                nbr += 1
        elif j+1 == length and 1 <= i <= height-2:
            for x in [i-1,i+1]:
                for y in [j-1,j]:
                    if ins[x][y] == "#":
                        nbr += 1
            if ins[i][j-1] == "#":
                nbr += 1
        elif 1 <= i <= height-2 and 1 <= j <= length-2:
            for x in [i-1,i+1]:
                for y in [j-1,j+1]:
                    if ins[x][y] == "#":
                        nbr += 1
            if ins[i][j-1] == "#":
                nbr += 1
            if ins[i-1][j] == "#":
                nbr += 1
            if ins[i][j+1] == "#":
                nbr += 1
            if ins[i+1][j] == "#":
                nbr += 1
    return nbr
for i in range(height):
    tmp = []
    for j in range(length):
        if ins[i][j] == "L":
            tmp.append("#")
        else:
            tmp.append(ins[i][j])
    ins[i] = tmp
while True:
    a, gl,adj = 0,0, []
    for i in range(height):
        for j in range(length):
            if ins[i][j] == "#":
                a += 1
    for i in range(height):
        new = []
        for j in range(length):
            new.append(findadj(i,j))
        adj.append(new)
    for i in range(height):
        tmp = []
        for j in range(length):
            if adj[i][j] >= 4 and ins[i][j] == "#":
                tmp.append("L")
            elif adj[i][j] == 0 and ins[i][j] == "L":
                tmp.append("#")
            else:
                tmp.append(ins[i][j])
        ins[i] = tmp
    for i in range(height):
        for j in range(length):
            if ins[i][j] == "#":
                gl += 1
    if gl == a:
        print(gl)
        break
