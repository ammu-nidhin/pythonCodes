inputString=input("Enter the String\n")
str=''
for i in range(0,len(inputString)):
    if i%2==0 and inputString[i].isalpha() :
        str=str+inputString[i]
print(str)
