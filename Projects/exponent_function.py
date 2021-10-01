def exponential(base,power):
    result = 1
    for index in range(power):
        result = result*base
    return result



if __name__ == "__main__":
    print(exponential(2,0))
