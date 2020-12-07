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
            temp = d[i].split(" ")
            if temp[len(temp)-1] == "bag":
                d[i] = d[i][:-4]
            elif temp[len(temp)-1] == "bags":
                d[i] = d[i][:-5]
        data[b] = d
def BFS(G,start):
    Q = deque()
    discovered = set()
    Q.append(start)
    counter = 0
    while Q:
        v = Q.popleft()
        if not v in discovered and not v == "no other":
            for i in G[v[2:]]:
                if v != start:
                    for j in range(int(v[0])):
                        Q.append(i)
                        print(i)
                else:
                    Q.append(i)
                #    discovered.add(i)
                counter += int(v[0])
        if v == "no other":
            counter += 1
    return counter
total = 0
for j in data["shiny gold"]:
    total = BFS(data,j)
print(total)
