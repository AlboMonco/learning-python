from math import pow
def calculator():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Which operation do you want to use?\nPress 1 for multiplication\n2 for addition\n3 for division\n4 for exponential: ")
    if operation == 1:
        return num1*num2
    elif operation == 2:
        return num1 + num2
    elif operation == 3:
        return num1/num2
    elif operation == 4:
        return pow(num1, num2)
    else:
        return "This is not one of the choices"
    
if __name__ == "__main__":
    calculator()
    pass