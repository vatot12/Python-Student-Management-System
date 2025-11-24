def add_student(students_list):
    student_name = str(input("What is the students name?:   "))
    try:
        math = int(input("Math?"))
        science = int(input("Science?"))
        english = int(input("English?"))
    except ValueError:
        pass
    try:
        if isinstance(math, int) and isinstance(science, int) and isinstance(english, int) and isinstance(student_name, str):
            students_list.append({"name": student_name, "Math": math, "Science": science, "English": english})
            student_added = True
            print("Student has been added")
    except UnboundLocalError:
        print("Student could not be added as you did not enter a number/name")
        student_added = False
    return student_added

def get_student_average(students_list):
    averaged = False
    student_averaged = input("Enter student's name")
    for i in students_list:
        if i["name"] == student_averaged:
            avg_step = i["Math"] + i["Science"] + i["English"]
            average = avg_step / 3
            print(f"{i["name"]}'s Average is {average}")
            averaged = True
        if averaged == False:
            print("Not found")


def remove_student(students_list):
    try:
        student_remove = str(input("Student name? (Case sensitive)"))
        for i in students_list:
            if student_remove in i["name"]:
                students_list.remove(i)
                removed = True
                print("Student removed")
                break
            else:
                removed = False
        if removed == False:
            print("Student isn't in your list")
    except ValueError:
        print("Student could not be removed as you entered a number")

def update_grades(students_list):
    student_update = input("What is the student name?")
    try:
        for i in students_list:
            if student_update == i["name"]:
                new_math = int(input("Math?"))
                new_sci = int(input("Science?"))
                new_eng = int(input("English?"))
                i["Math"] = new_math
                i["Science"] = new_sci
                i["English"] = new_eng
                print("Student grades changed successfully")
                print(f"New grades: {students_list}")
                found = True
                break
            else:
                found= False
        if found == False:
            print("Not found")
    except ValueError:
        print("Values error")

def list_all_students(students_list):
    for i in students_list:
        print(f"{i["name"]}: Math: {i["Math"]}, Science: {i["Science"]}, English:{i["English"]}")
    if students_list == []:
        print("Empty list")



def find_top_student(students_list):
    for i in students_list:
        avg_step = i["Math"] + i["Science"] + i["English"]
        avg = avg_step / 3
        i["Average"] = avg
    highest_num = 0
    highest_name = ""
    for i in students_list:
        if i["Average"] > highest_num:
            highest_num = i["Average"]
            highest_name = i["name"]
    print(f"{highest_name}'s average is the highest with {highest_num}")

students = []

while True:
    print("""
1. Add student
2. Remove student
3. Update grades
4. Get student average
5. List all students
6. Find top student
7. Quit
""")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        remove_student(students)
    elif choice == "3":
        update_grades(students)
    elif choice == "4":
        get_student_average(students)
    elif choice == "5":
        list_all_students(students)
    elif choice == "6":
        find_top_student(students)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
