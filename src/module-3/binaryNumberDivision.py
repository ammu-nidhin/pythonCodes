newList=[]
num=[x for x in input("Enter four digit binary number:\n").split(",")]
for ele in num:
    'binary conversion'
    value=int(ele,2)
    if(value%5==0):
        newList.append(ele)
print(','.join(newList))

