is_male = False
if not(is_male):
    print("not male")
if is_male:
    print("male")
if is_male == True:
    print("male")


#If the thing in "if" is true, you don't need to put "==".
# you can also do the following architecture:
#logic conjunctions: "and", "or", "not(element)". (Boolean things) 
#if, elif, else.


#Comparisons:
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    else:
        if num2 >= num3:
            return num2
        elif num2 <= num3:
            return num3

if __name__ == "__main__":
    print(max_num(1,2,3))
            
