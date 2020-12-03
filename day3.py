k = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for t in lines:
    k.append(t.replace("\n",""))
t = len(k)
for i in range(0,len(k)):
    k[i] = k[i] * int(len(k)/3)
trees = [0,0,0,0,0]
for i in range(1,len(k), 1):
    for j in range(i,i + 1,1):
        if k[i][j] == "#":
            trees[0] = trees[0] + 1
    for j in range(3*i,3*i + 3,3):
        if k[i][j] == "#":
            print(k[i][j],i,j)
            trees[1] = trees[1] + 1
    for j in range(5*i,5*i + 5,5):
        if k[i][j] == "#":
            trees[2] = trees[2] + 1
    for j in range(7*i,7*i + 7,7):
        if k[i][j] == "#":
            trees[3] = trees[3] + 1
for i in range(2,len(k), 2):
    for j in range(int(i/2),int(i/2) + 1,1):
        if k[i][j] == "#":
            trees[4] = trees[4] + 1
mult = 1
for i in trees:
    mult = mult * i

print(mult)
