ins = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        ins.append(line.replace("\n",  ""))
for i in range(26,len(ins)):
    found = False
    x,y = 0,0
    for j in range(0+(i-26),26+(i-26)):
        for z in range(i-26,j):
            if int(ins[j]) + int(ins[z]) == int(ins[i]):
                found = True
                break
    if not found:
        invalid = int(ins[i])
        for j in range(0,i):
            sum = int(ins[j])
            ele = [int(ins[j])]
            for z in range(j+1,i):
                if sum < invalid:
                    sum += int(ins[z])
                    ele.append(int(ins[z]))
                elif sum == invalid:
                    print(min(ele)+ max(ele))
                    break
                else:
                    break
