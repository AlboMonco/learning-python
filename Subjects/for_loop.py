import string

list = ["a","b","c","d","e","f","g","h","i","1","2","3","4","5"]
for letter in "Cake":
    print(letter)
 
result = [letter for letter in list if letter in string.ascii_letters]



