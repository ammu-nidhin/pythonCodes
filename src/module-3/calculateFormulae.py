
import math

def calFormulae(d):
    c = 50
    h = 30
    q=int(math.sqrt((2*c*d)/h))
    return q

d=list(map(int,input("Enter three values:\n").split(",")))
numList=list(map(calFormulae,d))
print(str(numList).strip("[]"))