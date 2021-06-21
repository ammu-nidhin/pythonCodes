str1=input("Enter the string sequence:\n")
inputList=list(str1.split(" "))
inputList.sort()
finalList=[]
checkduplicate=set()
for ele in inputList:
    if ele in checkduplicate:
        continue
    else:
        finalList.append(ele)
        checkduplicate.add(ele)
print(' '.join(finalList))