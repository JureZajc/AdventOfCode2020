file = open("./inputs/input4.txt", "r")
list = file.readlines()

count = 0

#for first part and second part as well , "cid": 0 is optional so we just remove it
propertiesDict = {"byr" : 0, "iyr" : 0, "eyr" : 0, "hgt" : 0, "hcl" : 0,
"ecl" : 0, "pid" : 0} 

for i in list:
    if i == "\n":
        propertiesDict = dict.fromkeys(propertiesDict,0)
        continue
    else:
        split = i.split()
        countSplit = len(split)
        for j in split:
            #print(j[0:3])
            if j[0:3] in propertiesDict:
                propertiesDict[j[0:3]] = j[4:] #change this to 1 for 1st part
                #if all(x==1 for x in propertiesDict.values()): #only for first part
                if 1920 <= int(propertiesDict["byr"]) <= 2002:
                    if 2010 <= int(propertiesDict['iyr']) <= 2020:
                        if 2020 <= int(propertiesDict['eyr']) <= 2030:
                            if propertiesDict['ecl'] in ['amb', 'blu', 'gry', 'brn', 'hzl', 'grn', 'oth']:
                                if propertiesDict['hgt'] != 0:
                                    if propertiesDict['hgt'][-2:] == "cm" and 150 <= int(propertiesDict['hgt'][:-2]) <= 193 or propertiesDict['hgt'][-2:] == "in" and 59 <= int(propertiesDict['hgt'][:-2]) <= 76:
                                        if propertiesDict['hcl'] != 0:
                                            if propertiesDict['hcl'][0] == "#" and propertiesDict['hcl'][1] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] and propertiesDict['hcl'][2] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] and propertiesDict['hcl'][3] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] and propertiesDict['hcl'][4] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] and propertiesDict['hcl'][5] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'] and propertiesDict['hcl'][6] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                                                if propertiesDict['pid'] != 0:
                                                    if len(propertiesDict['pid']) == 9:
                                                        if propertiesDict['pid'][0] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][1] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][2] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][3] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][4] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][5] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][6] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][7] in ['0','1','2','3','4','5','6','7','8','9'] and propertiesDict['pid'][8] in ['0','1','2','3','4','5','6','7','8','9']:
                                                            count+=1
                                            
                    
print(count)



