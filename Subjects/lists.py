#lists: Structure to store information to organize them and to manage them

letters = ["a","b","c","d","e","f","g"]
#Index:     0   1   2   3   4   5   6
#Index:    -7  -6  -5  -4  -3  -2  -1


#Functions: Access to some element in the list: name_list[index]; name_list[index1:index2] - gives me all the elements in the list starting in index1 and finishing in index2.
#If there is not an index2, the program will give all the elements starting in index1 until the end.
#I can change the element of a list: if I want to change the letter c by the letter h, these are the steps: letters[2] = "h" or letters[-5]= "h"
#letters.extend(list or str) will extend your original list by the information that you give. If you use letters.extend(list), the list that you created before will be add in the letters(without brackets).
#letters.append(list or str or int or boolean) will add the information to the letters. If you use letters.append(list), the list that you created before will be add in the letters (with brackets)
#letters.insert(index, element) will insert in the index the element of the second parameter, and will pull the others elements in the list to the right. Example: letters.insert(1,"h"). The letters will be: letters = ["a","h","b","c","d","e","f","g"]
#letters.remove(element) will remove the element from the list. I can use letters.remove(letters[index]) if I want to remove the element with the index.
#letters.clear() will remove all the elements from your list.
#letters.pop() will remove the last element in the list (index = -1)
#letters.index(element) will return the index of the element. It's useful to check if an element is or not in the list.
#letters.count(element) will count how many times this element appears in the list.
#letters.sort() will sort the list in the ascending order and return None.
#letters.reverse() will reverse the order of the list.
#letters2 = letters.copy() will copy the list "letters" and will give to "letters2" the same elements. They will be equal.
#