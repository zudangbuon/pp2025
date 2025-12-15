student = []
course = []
marks = {}

#input functions
def input_number_of_student():
    n = int(input("Enter number of student: "))
    return n

def input_student(n):
    for i in range(n):
        sID = input(("Student ID: "))
        name = input(("Student name: "))
        dob = input(("Date of birthday: "))
        print("\n")
        student.append({"id": sID, "name": name, "dob": dob})

def intput_number_of_course():
    n = int(input("Enter number of course: "))
    return n

def input_course(n):
    for i in range(n):
        cID = input("Course ID: ")
        cName = input("Course name: ")
        course.append({"id": cID, "name": cName})

def input_mark():
    print("\nCourses:")
    for c in course:
        print(c["id"], "-", c["name"])

    course_id = input("Choose course ID: ")

    for s in student:
        mark = float(input("Enter mark for " + s["name"] + ": "))
        marks[(s["id"], course_id)] = mark

#listing functions
def list_student():
    print("\nStudent list:")
    for s in student:
        print(s["id"], s["name"], s["dob"])

def list_course():
    print("\nCourse list:")
    for c in course:
        print(c["id"], c["name"])

def show_mark():
    course_id = input("Enter course ID: ")
    print("\nMark: ")
    for s in student:
        key = (s["id"], course_id)
        if key in marks:
            print(s["name"], ": ", marks[key])
        else:
            print(s["name"], ": No mark")

#main
def main():
    n = input_number_of_student()
    input_student(n)

    m = intput_number_of_course()
    input_course(m)

    input_mark()
    list_student()
    list_course()
    show_mark()

main()