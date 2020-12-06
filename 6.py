file = open("./inputs/input6.txt", "r")
list = file.readlines()

answers = set()
count = 0
countIntersection = 0
everyoneAnswers = set()
first = True

for i in list:
    for j in i[:-1]:
        answers.add(j)
    if i == "\n":
        count += len(answers)
        answers.clear()
        countIntersection += len(everyoneAnswers)
        everyoneAnswers.clear()
        first = True
    elif first:
        for k in i[:-1]:
            everyoneAnswers.add(k)
        first = False    
    else:
        thisPerson = set()
        for t in i[:-1]:
            thisPerson.add(t)
        everyoneAnswers = everyoneAnswers.intersection(thisPerson)



count += len(answers)
countIntersection += len(everyoneAnswers)      
print("Count for first part: " + str(count) + ".")
print("Count intersection is: " + str(countIntersection) + ".")