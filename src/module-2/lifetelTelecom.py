from cryptography.fernet import Fernet
import re

str = input("Enter the id\n")
if len(str) < 12:
    print("The Reference Id should be minimum 12 digits")
else:
    if re.search("[a-zA-Z]", str):
        if re.search("[0-9]", str):
            if re.search("[$@#]", str):
                str = str.encode()
                key = Fernet.generate_key()
                f = Fernet(key)
                cipher = f.encrypt(str)
                print("Your Reference Id is:")
                print(cipher)

                option = input("Do you want to decrypt your reference Id ? Press 'Yes' or 'No':\n")
                if option == 'yes':
                    message = f.decrypt(cipher)
                    print(message.decode())

            else:
                print("The Reference Id should have any one special charater $ ,@,#")
        else:
            print("The Reference Id should have digits")
    else:
        print("The Reference Id should have alphabets")

