list = [input() for _ in range(617)]


emptyList = []
for i in list:
    inp = i.split()
    emptyList.append([inp[0], int(inp[1])])

def firstPart():
    acc = 0
    visited = [0 for j in range(len(emptyList))]
    counter = 0
    flag = True
    while flag:
        if counter == len(emptyList):
            print("We are finished")
            break
        if visited[counter]:
            print("Infinity loop")
            flag = False
            break
        visited[counter] = 1
        if emptyList[counter][0] == "nop":
            counter += 1
        elif emptyList[counter][0] == "acc":
            acc += emptyList[counter][1]
            counter += 1
        else:
            counter += emptyList[counter][1]
    return visited, acc, flag

visitedFirst, acc, flag = firstPart()
print(acc)

#2nd part
for i, j in enumerate(visitedFirst):
    if j == 1 and emptyList[i][0] == "jmp":
        emptyList[i][0] = "nop"
        a, acc, flag = firstPart()
        if flag == True:
            print(acc)
            break
        else:
            emptyList[i][0] = "jmp"

    if j == 1 and emptyList[i][0] == "nop":
        emptyList[i][0] = "jmp"
        a, acc, flag = firstPart()
        if flag == True:
            print(acc)
            break
        else:
            emptyList[i][0] = "nop"
            


