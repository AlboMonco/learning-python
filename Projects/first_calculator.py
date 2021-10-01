from math import pow
def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = int(input("Which operation do you want to use?\nPress 1 for multiplication\n2 for addition\n3 for division\n4 for exponential: "))
    if operation == 1:
        return num1*num2
    elif operation == 2:
        return num1 + num2
    elif operation == 3:
        if num2 == 0:
            return "Can't determine"
        else:
            return num1/num2
    elif operation == 4:
        if num1 == 0 and num2 == 0:
            return "Can't determine"
        else: 
            return pow(num1, num2)
    else:
        return "This is not a number of an operation. Please try again."


if __name__ == "__main__":
    print(calculator())