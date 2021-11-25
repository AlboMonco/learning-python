def repetitor(list:list):
    list2 = []
    for element in list:
        if element not in list2:
            list2.append(element)
    return list2

def counter(list:list):
    dict = {}
    for element in list:
        if element not in dict:
            dict[element] = 1
        else:
            dict[element] += 1
    return dict




if __name__ == "__main__":
    print(counter([1,2,2,2,2,2,2,3,3,3,3,3,3,3]))

