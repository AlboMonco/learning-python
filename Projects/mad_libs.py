def mad_libs():
    color = str(input("Give a color: "))
    plural_noun = str(input("Give a plural noun: "))
    food = str(input("Give me a food: "))

    phrase = "Roses are " + color + "\n" + plural_noun + " are blue\nI love " + food
    return phrase


if __name__ == "__main__":
    print(mad_libs())
