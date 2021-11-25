def invert_string(string:str):
    other_string = ""
    for index in range(len(string)-1,-1, -1):
        other_string += string[index]
    return other_string

def palindromic(string:int or str):
    if str(string) == invert_string(str(string)):
        return True
    else:
        return False

def largest_palindromic():
    



if __name__ == "__main__":
    print(palindromic(9009)) 
    





#abcd -> dcba