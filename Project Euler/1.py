def sumer(last_number:int, first_number:int, second_number:int):
    numbers = []
    for number in range (0, last_number+1):
        if number%first_number == 0 or number%second_number == 0:
            numbers.append(number) 
    return numbers, sum(numbers) 



if __name__ == "__main__":
    print(sumer(1000,3,5))
