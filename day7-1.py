from collections import deque
data = dict()
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        applicable = line.replace("\n","").split(" bags contain ")
        b,d = applicable[0].rstrip(),applicable[1][:-1]
        d = d.split(", ")
        for i in range(len(d)):
            d[i] = d[i][2:]
            temp = d[i].split(" ")
            if temp[len(temp)-1] == "bag":
                d[i] = d[i][:-4]
            elif temp[len(temp)-1] == "bags":
                d[i] = d[i][:-5]
        data[b] = d
def BFS(G,start):
    Q = deque()
    discovered = set()
    neighbors = dict()
    Q.append(start)
    while Q:
        v = Q.popleft()
        if not v in discovered and not v == " other":
            for i in G[v]:
                if i == "shiny gold":
                    return 1
                Q.append(i)
                discovered.add(v)
    return 0
total = 0
for i in data:
    total += BFS(data,i)
print(total)
