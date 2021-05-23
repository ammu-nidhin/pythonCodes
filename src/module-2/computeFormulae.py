num=int(input("Enter a number:\n"))
if num>0:
    sum=0.0
    for i in range(1,num+1):
        sum=sum+(i/(i+1))
    print(round(sum,2))
else:
    print("The number should be greater than 0")