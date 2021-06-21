dataList=['analytics','machine learning','python','xyz']
searchData=input("Enter the data to search:\n")
if searchData.lower() in dataList:
    print("Data is present")
else:
    print("Data not present")