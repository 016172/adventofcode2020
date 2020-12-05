#-----------Part 1--------------
# import sys
# k = []
# valid = 0
# with open('input.txt', 'r') as file:
#    lines = file.readlines()
# for t in lines:
#     k.append(t.replace("\n",""))
# for j in k:
#     i,l,p = j.split()
#     mi,ma = [int(x) for x in i.split("-")]
#     l = l.split(":")[0]
#     z = p.count(l)
#     if mi <= z and z <= ma:
#         valid = valid + 1
#
# print(valid)
#-------------Part 2-----------------
k = []
valid = 0
with open('input.txt', 'r') as file:
   lines = file.readlines()
for t in lines:
    k.append(t.replace("\n",""))
for j in k:
     i,l,p = j.split()
     l = l.split(":")[0]
     mi,ma = [int(x) for x in i.split("-")]
     print(p,i,p[mi-1] == l, p[ma-1] == l, l)
     if (p[mi-1] == l) and (not p[ma-1] == l):
         valid = valid + 1
     elif (not p[mi-1] == l) and (p[ma-1] == l):
         valid = valid + 1
print(valid)
