import random
#"\" is used to put other information in next line
def guess_number():
    print("Hello! What is your name?")
    name = input()
    print("Well, {}, I'm thinking a number between 1 and 20".format(name))
    secret_number = \
    random.randint(1,20)
    for guesses in range(1,7):
        print("Take a guess:")
        guess = int(input())
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            break
    if guess == secret_number:
        print("You won! Congratulations: You have guesses correctly in {} guesses".format(guesses))
    else:
        print("You lost: out of guesses")

if __name__ == "__main__":
    print(guess_number())