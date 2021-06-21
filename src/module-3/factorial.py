def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    # print(fact)


if __name__ == "__main__":
    print("Enter the number:\n")
    num = int(input())
    # print(num)
    res = factorial(num)
    print("The factorial of "+str(num) + "\tis\t" + str(res))
