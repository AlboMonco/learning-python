#Dictionaries: key values pairs.

#I want to convert Jan -> January, Mar -> March, Sep -> September

month_names = {"Jan": "January", "Mar": "March", "Sep": "September"}

#All the keys are unique.
#The keys can be anything (str, int , float, etc)
#There are different ways to have access in the dictionary's keys:
#By the key: month_names["Jan"]
#By the key: month_names.get("Jan")
#month_names.get("Luv", "Not a valid key")
#month_names["Feb"] = "February"
#del month_names["key"] will remove the key from the dictionary