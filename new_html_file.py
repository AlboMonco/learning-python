import os
base_path = os.path.join("C:\\","Users","HP","Code","learning-python","Subjects")

file = open(os.path.join(base_path,"index.html"),"w")

file.write("<p>This is a HTML file</p>")

file.close()

