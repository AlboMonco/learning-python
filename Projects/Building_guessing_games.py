def guess_word():
    secret_word = "tonho"
    guess = input("Guess a word. You have 3 chances: ")
    guess_count = 1
    guess_limit = 3
    while guess != secret_word:
        guess = input("Wrong! Guess another word or press 0 for exit. You have 1 chance: ") if guess_count == 2 else input("Wrong! Guess another word or press 0 for exit. You have {} chances: ".format(guess_limit-guess_count))
        guess_count += 1
        if guess == "0": break
        else:
            if guess_count == guess_limit:
                return "You lost!"
    return "Congratulations!"
if __name__ == "__main__":
    print(guess_word())