
upperCaseCount=0
lowerCaseCount=0
inputString=input("Enter the sentence ith both capital letter and small letters:\n")
for i in inputString:
    if i.isalpha():
        if i.islower():
            lowerCaseCount+=1
        elif i.isupper():
            upperCaseCount+=1
        else:
            continue
print("UpperCase:\t",upperCaseCount)
print("LowerCase:\t",lowerCaseCount)
