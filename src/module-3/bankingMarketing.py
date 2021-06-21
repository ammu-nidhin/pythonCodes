

import csv

professionList=set()
age=set()
with open('bank-data.csv',mode='r') as file:
    csvFile=csv.DictReader(file)
    for lines in csvFile:
        professionList.add(lines['Profession'].lower())
        age.add(lines['Age'])
sortedAge=sorted(age)
minMaxAge={"minAge":min(sortedAge),"maxAge":max(sortedAge)}

profession=input("Enter your Profession and to exit enter 'END':\n")
while(profession.lower()!='end'):
    ageCheck=input("Enter your age:\n")
    if professionList.__contains__(profession.lower()) and (ageCheck>=minMaxAge['minAge'] and ageCheck<=minMaxAge['maxAge']):
        print("You are eligible for loan")
    else:
        print("Sorry you are not eligible for loan")
    profession=input("Enter your profession:\n")
print("Thank you!\n")
