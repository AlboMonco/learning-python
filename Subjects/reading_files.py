import os

base_path = os.path.join("C:\\", "Users", "HP", "Code", "learning-python", "Subjects")

file = open(os.path.join(base_path,"text.txt"),"r")

#r - read, w - write, r+ - read and write, a - append some information to the file
#file.read() reads the file; file.readable() checks if the file is readable; file.close() closes the file. file.readline() will read the first line, and if i put after this function the same function, it will read the line that comes afterwards.
#file.readlines()[index](the index gives the thing written in the position, starting with 0) put all the thing of the file inside a list

for employee in file.readlines():
    print(employee)

file.close()
