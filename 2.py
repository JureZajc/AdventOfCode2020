list = [input() for _ in range(1000)]

# 1st part and 2nd part
count = 0
count2 = 0

for i in list:
    s = i.split()
    numberSplit = s[0].split('-')
    charValue = s[1][0]
    print(s[2][int(numberSplit[0])])
    if int(numberSplit[0]) <= int(s[2].count(charValue)) <= int(numberSplit[1]):
        count+=1
    if charValue == s[2][int(numberSplit[0])-1] and charValue != s[2][int(numberSplit[1])-1] or charValue != s[2][int(numberSplit[0])-1] and charValue == s[2][int(numberSplit[1])-1]:
        count2+=1
print(count)
print(count2)