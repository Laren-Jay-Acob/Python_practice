num = [1,2,2,3,4,5,5,6,7,8,8,9,10,10]
newList = []

for x in num:
    if x not in newList:
        newList.append(x)

print(newList)