class student:
    def __init__(self, name:str, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

class teacher:
    def __init__(self, name:str, age:int, subject:str):
        self.name = name
        self.age = age
        self.subject = subject

    def is_good(self, subject):
        if subject == "Matemática":
            return True
        else:
            return False
        
class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
