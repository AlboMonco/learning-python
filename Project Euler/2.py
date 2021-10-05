def fibonacci(parameter:int):
    Fibonacci = [1,2]
    for number in range(0, parameter+1):
        if number == Fibonacci[-1] + Fibonacci[-2]:
            Fibonacci.append(number)
    return Fibonacci

def sum_even(parameter:int):
    fibonacci_list = fibonacci(parameter)
    list = []
    for number in fibonacci_list:
        if number%2 == 0:
            list.append(number)
    return list, sum(list)
            





if __name__ == "__main__":
    print(sum_even(4000000))
