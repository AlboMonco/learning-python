from classes import teacher

def teacher_is_good(subject):
    teacher1 = teacher("Antonio",23,"Matemática")
    return teacher1.good(subject)
        



if __name__ == "__main__":
    print(teacher_is_good("Portugues"))