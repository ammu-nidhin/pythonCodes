import random
randNumList=[]
while len(randNumList)<5:
    randNum=random.randint(1,1000)
    if randNum%5==0 and randNum%7==0 and randNum not in randNumList:
        randNumList.append(randNum)
print(randNumList)