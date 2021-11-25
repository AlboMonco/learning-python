import string
#vowels -> y

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "y"
        else:
            translation = translation + letter
    return translation


if __name__ == "__main__":
    print(translate("abacate"))