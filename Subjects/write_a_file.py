import os
base_path = os.path.join("C:\\","Users","HP","Code","learning-python","Subjects")

file = open(os.path.join(base_path,"text2.txt"),"w")

file.write("Apagar tudo")

#the difference between "w" and "a" is this: "a" is used to append some new information to the file, and "w" is used to overwrite the file.

file.close()
