
import random
import re

def cashWithdraw():
    global currentbalance
    amtToWithdraw=int(input("Enter the amount to withdraw\n"))
    currentbalance = currentbalance - amtToWithdraw
    print("The amount ",amtToWithdraw ,"is withdrawn. Your current balance is ",currentbalance)

def cashCredit():
    global currentbalance
    amtToCredit=int(input("Ënter the amount to deposit\n"))
    currentbalance=currentbalance+amtToCredit
    print("The amount ",amtToCredit,"is credited. Your current balance is ",currentbalance)

def passwordCheck():
    valid=0
    while valid==0:
        pswd = input("Enter the new password")
        reg=r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@$#]).{6,12}"
        pattern=re.compile(reg)
        if(re.search(pattern,pswd)):
            valid=1
        else:
            print("Please enter a valid password.\n The password should have minimum 6 characters and maximum 12 characters.\n There should be atleast an alphabet and atleast an alphabet in capital, atleast one digit and altleast one special character #,$,@\n")
            valid=0
    return valid

def changePassword():
    value=passwordCheck()
    print("The password has been changed\n")

options=int(input("Enter 1:Cash withdraw\n 2: Cash Credit\n 3: Change Password \n 4: Exit\n"))

currentbalance=random.randrange(10000,100000)
while(options!=4):
    if(options==1):
        cashWithdraw()
    elif(options==2):
        cashCredit()
    elif(options==3):
        changePassword()
    else:
        print("Enter 1:Cash withdraw\n 2: Cash Credit\n 3: Change Password \n 4: Exit\n")
    options=int(input("Enter the option"))

print("Thank you for banking with us.\n")
