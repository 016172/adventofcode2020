k = []
persons = []
validc = 0
tempList = []
req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:

    if line != "\n":
        #print(line)
        line = line.replace(" ",",").replace("\n", "").split(",")
        #print(line)
        for j in line:
            tempList.append(j.split(":")[0])
    else:
        persons.append(tempList)
        print("new person" + str(tempList))
        tempList = []
print(len(persons))
for person in persons:
    if "cid" in person:
        if len(person)-1 == len(req):
            validc += 1
    else:
        if len(person) == len(req):
            validc += 1
print(validc)
