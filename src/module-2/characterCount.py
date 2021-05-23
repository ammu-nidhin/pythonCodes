inputString=input("Enter the string\n")
count=0
alphacount={}
for i in inputString:
    count=inputString.count(i)
    alphacount.update({i:count})
for i in alphacount:
    print("{},{}".format(i,alphacount[i]))
