# Main Program

def MainMenu():
    print("\nMain Menu")
    print("1. Add Student")
    print("2. Enroll Student in Course")
    print("3. Remove Student")
    print("4. View All Student")
    print("5. Search Student")
    print("6. Exit\n")
    
# Student Name Exist Checker

def NameChecker(name, students, data):
    if name in students:
        print("Student Already Exist.")
        return
    students.append(name) # appended to list
    data[name] = set() # add to dictionary
    print(f"Student {name} Successfully Added.")
    return

# Enroll Student
def StudentChecker(name, data):
    if name not in data:
        print("Student Does not Exist")
        return
    
    courseCode = input("Enter Course Code: ")
    courseName = input("Course Name: ")

    data[name].update([courseCode, courseName])
    print(f"Student {name} Enrolled to {courseCode} : {courseName}")
    return

# Remove Student
def RemoveStudent(name, students, data):
    if name not in students and name not in data:
        print(f"Student {name} does not Exist.")
        return
    students.remove(name)
    del data[name]
    print(f"Student {name} Successfully Removed.")
    return

# Show All Students
def PrintAllStudent(data):
    for name, course in data.items():
        print(f"Name: {name}\t Course: {course}")
    return
    
# Program (Start)

# variables
students = [] # lists of students
school_data = dict() # dict of students enrolled classes

while True:
    # Main Menu Choice
    MainMenu()
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please Input a valid Choice")
        continue
    
    # Choice Checker
    match choice:
        case 1:
            # Add Student
            name = input("Enter Student Name: ")
            NameChecker(name, students, school_data)
            continue # go back to menu
        
        case 2:
            # Enroll Student in Course
            name = input("Enter Student Name to Enroll: ")
            StudentChecker(name, school_data)
            continue

        case 3:
            # Delete Student from List and Dict
            name = input("Enter Student Name to Remove: ")
            RemoveStudent(name, students, school_data)
            continue
        
        case 4:
            # Show All Students
            PrintAllStudent(school_data)
            continue

        case 5:
            pass
        case 6:
            break