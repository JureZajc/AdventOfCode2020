list = [input() for _ in range(323)]
width = len(list[0])

count3 = 0
count1 = 0
count5 = 0
count7 = 0
count11 = 0
flag = False
position3 = 3
position1 = 1
position5 = 5
position7 = 7
position11 = 1
for i in list[1:]:
    if i[position3] == '#':
        count3+=1
    if i[position1] =='#':
        count1 +=1
    if i[position5] =='#':
        count5+=1
    if i[position7] == '#':
        count7+=1
    if flag:
        if i[position11] =='#':
            count11 +=1
        position11 += 1
        position11 %= width    
        flag = False
    else:
        flag = True
    position3+=3
    position3 %= width
    position1+=1
    position1 %= width
    position5+=5
    position5 %= width
    position7+=7
    position7 %= width
 
print(count3*count1*count5*count7*count11)