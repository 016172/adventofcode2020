import sys
k = []
with open('input.txt', 'r') as file:
   lines = file.readlines()
for t in lines:
    k.append(int(t.replace("\n","")))
print(k)
for p in range(0,len(k)):
    for z in range(0,p):
        for k in range(0,p)
        if k[p] + k[z] == 2020:
            print(k[p]*k[z])
            break
