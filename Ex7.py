def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    for name in studentNames:
        print(name + " Evans")
    return studentNames

def addToList(studentNames):
    new_name = input("Please enter another name to add to the list: ")
    studentNames.append(new_name)
    for name in studentNames:
        print(name + " Evans")

if __name__ == "__main__":
    names_list = studList()
    addToList(names_list)
