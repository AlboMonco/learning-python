def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        return "Error: Division by Zero"


def sandwich():
    global eggs 
    eggs = 4
    return eggs





if __name__ == "__main__":
    print(div42by(2))
    print(sandwich())
    print(eggs)