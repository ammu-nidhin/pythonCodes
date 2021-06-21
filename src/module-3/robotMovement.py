import math

x = 0
y = 0
cord = [0, 0]
orgin = [x, y]
str = int(input("Enter 1: Move robot up\n 2: Move robot down\n 3: Move robot left\n 4:move robot right\n 5: to exit\n"))
while (str !=5):
    if str == 1:
        y = y + 5
        orgin = [x, y]

    elif str == 2:
        y = y - 3
        orgin = [x, y]

    elif str == 3:
        x = x - 3
        orgin = [x, y]

    elif str == 4:
        x = x + 2
        orgin = [x, y]

    else:
        print("Enter a number between 1 to 4\n")

    str=int(input("Enter the option\n"))

print("The current coordinate of robot",orgin)
print("The distance robort moved : ",math.dist(orgin, cord))
