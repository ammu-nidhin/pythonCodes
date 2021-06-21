

def twoDArray(r,c):
    arrayElement=[]
    for i in range(0,r):
        ele = []
        for j in range (0,c):
            num=i*j
            ele.append(num)
        arrayElement.append(ele)
    return arrayElement

row,col=[int(x) for x in input("Enter two numbers:\n").split(',')]
matrixElement=list(twoDArray(row,col))
print(matrixElement)