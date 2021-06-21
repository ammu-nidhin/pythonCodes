
import csv
import re
from customer import Customer
from customerNotAllowedException import CustomerNotAllowedException
from order import Order



def splitFullName(name):
    nameList=re.split(r"[.\s]",name)
    title=nameList[0]
    firstName=nameList[1]
    lastName=nameList[2]
    return title,firstName,lastName

def createOrder(customerObj):

    fullname=customerObj.firstName+customerObj.lastName

    try:
        if(customerObj.getBlacklisted()=="1"):
            raise CustomerNotAllowedException(fullname)
    except CustomerNotAllowedException as err:
        print(err.message)

    if customerObj.getBlacklisted()=="0":
        print("Enter the order details for",fullname,":\n")
        pname = input("Enter the product name:\n")
        pcode = input("Enter the product code:\n")
        print("The customer ",fullname,"is eligible. The order created.\n")
        return Order(pname, pcode)


def main():
    customerobjectList=[]
    with open('fairDealCustomer-data.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            title,fname,lname=splitFullName(lines['Fullname'])
            blackListed=lines['Blacklist']
            customerobjectList.append(Customer(title, fname, lname, blackListed))
    for obj in customerobjectList:
        createOrder(obj)


if __name__=="__main__":
    main()