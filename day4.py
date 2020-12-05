k = []
persons = []
validc = 0
tempList = []
req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        line = [i.split(":")[0] for i in line.split()]
        for z in line:
            tempList.append(z)
    else:
        persons.append(tempList)
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
