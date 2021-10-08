def fibonacci(parameter:int):
    Fibonacci = [1,1]
    for number in range(0, parameter+1):
        if number == Fibonacci[-1] + Fibonacci[-2]:
            Fibonacci.append(number)
    return Fibonacci

def sum_even(parameter:int):
    fibonacci_list = fibonacci(parameter)
    sum = 0
    for number in fibonacci_list:
        if number%2 == 0:
            sum += number
    return sum

def number_in_fibonacci(number:int):
    list = fibonacci(number)
    return True if number in list else False



def guess_what_Ines_is_gonna_to_say():
    print("Te amo<3")



if __name__ == "__main__":
    print(number_in_fibonacci(8))

    #print(guess_what_Ines_is_gonna_to_say())
