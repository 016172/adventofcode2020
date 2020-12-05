k = []
persons = []
validc = 0
tempList = []
req = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
with open('input.txt', 'r') as file:
    lines = file.readlines()
for line in lines:
    if line != "\n":
        line = [i.split(":") for i in line.split()]
        for z in line:
            tempList.append([z[0],z[1]])
    else:
        persons.append(tempList)
        tempList = []
for person in persons:
    person = [tup for tup in person if tup[0] != "cid"]
    if (len(person) >= len(req)):
        cc = 0
        for i in person:
            c,v = i[0],i[1]
            if c == "byr":
                if int(v) <= 2002 and int(v) >= 1920:
                    cc += 1
            elif c == "iyr":
                if int(v) >= 2010 and int(v) <= 2020:
                    cc += 1
            elif c == "eyr":
                if int(v) >= 2020 and int(v) <= 2030:
                    cc += 1
            elif c == "hgt":
                if v[3:] == "cm":
                    if int(v[:3]) >= 150 and int(v[:3]) <= 193:
                        cc += 1
                elif v[2:] == "in":
                    if int(v[:2]) >= 59 and int(v[:2]) <= 76:
                        cc += 1
            elif c == "hcl":
                if v[0] == "#":
                    if len(v.split("#")[1]) == 6:
                        cc += 1
            elif c == "ecl":
                if v in ["amb","blu","brn","gry","grn","hzl","oth"]:
                    cc += 1
            elif c == "pid":
                if v.isdecimal() and len(v) == 9:
                    cc += 1
        if cc == 7:
            validc += 1
print(validc)
