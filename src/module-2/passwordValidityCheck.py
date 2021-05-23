import re
pswd=input("Enter the password \n")
if len(pswd)>=6 and len(pswd)<=12:
    if (re.search("[a-z]",pswd)):
        if(re.search("[A-Z]",pswd)):
            if(re.search("[0-9]",pswd)):
                if(re.search("[$#@]",pswd)):
                    print("valid password")
                else:
                    print("The password should have atleast one character from $ ,# ,@")
            else:
                print("Atleast one digit required")
        else:
            print("Atleast one alphabet should be capital")
    else:
        print("Atleast one alphabet required")
else:
    print("password should have a minimum length  of 6 characters and a maximum length of 12 characters")