inputList=[12,24,35,24,88,120,155,88,120,155]
finalList=[]
checkDuplicate=set()
for ele in inputList:
    if ele in checkDuplicate:
        continue
    else:
        finalList.append(ele)
        checkDuplicate.add(ele)
print(finalList)

