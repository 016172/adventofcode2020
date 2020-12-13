ins,waittime = [],[]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
busses = ins[0].split(',')
offset = []
def euclides_extended_algorithm(z,n):
    if z == 0:
        return 0,1
    z1,n1 = euclides_extended_algorithm(n%z,z)
    t1 = n1 - (n//z) * z1
    t2 = z1
    return t1,t2
for i in range(len(busses)):
    offset.append((busses[i],i))
offset = [(int(_[0]),_[1]) for _ in offset if _[0] != 'x']
M = 1
a,bprime,b,m = [],[],[],[]
for i in offset:
    M = M * i[0]
    a.append(-i[1]%i[0])
    m.append(i[0])
for i in offset:
    b.append(M//i[0])
for i in range(len(offset)):
    bprime.append(euclides_extended_algorithm(b[i],m[i])[0]%m[i])
sum = 0
for z in range(len(bprime)):
    sum += a[z]*b[z]*bprime[z]
print(sum%M)
