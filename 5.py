list = [input() for _ in range(940)]

zone = [0,127]
zone2 = [0,7]
maximum = 0

airplane = [[0 for _ in range(8)] for _ in range(128)]
#print(airplane) #visualization of plane


def binarySearch(i, j, dirrection):
    if dirrection == 'F':
        return [i, (i+j)//2]
    else:
        return [(i+j)//2+1, j]

def binarySearch2(i, j, dirrection):
    if dirrection == 'L':
        return [i, (i+j)//2]
    else:
        return [(i+j)//2+1, j]

for i in list:
    for j in i[:6]:
        zone = binarySearch(zone[0], zone[1], j)
    if i[6] == "F":
        zone = zone[0]
    else:
        zone = zone[1]    
    for j in i[7:9]:
        zone2 = binarySearch2(zone2[0], zone2[1], j)
    if i[9] == 'R':
        zone2 = zone2[1]
    else:
        zone2 = zone2[0]  
    maximum = max(maximum, zone*8+zone2)
    airplane[zone][zone2] = 1
    zone = [0,127]
    zone2 = [0,7]
print(airplane) #your seat is where 0 is in the middle of the plane :)
print(maximum)

counter = 10

for i in airplane[10:]:
    if '.' in i:

        print(counter*8+i.index('.'))
        break

    counter+= 1
    
    