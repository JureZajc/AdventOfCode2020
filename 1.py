list = [int(input()) for _ in range(200)]
list.sort()

# 1st part
for i,j in enumerate(list):
    for k in list[i:]:
        if j + k == 2020:
            print(j * k)

# 2nd part
for i, j in enumerate(list):
    for k, l in enumerate(list[i:]):
        for m in list[k:]:
            if j + l + m == 2020:
                print(j * l * m)
