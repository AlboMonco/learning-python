def loop_demonstration():
    while True:
        print("Enter your name:")
        name = input()
        if name == "your name":
            break                       
    print("Thank you!")

def loop(): 
    message = 0
    while message < 5:
        message += 1
        if message == 3 or message == 2:
            continue
        print(message)



if __name__ == "__main__":
    loop()


