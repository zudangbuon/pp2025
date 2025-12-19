class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def get_student_id(self):
        return self.__student_id
    
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob
    
    def set_dob(self, dob):
        self.__dob = dob

    def display(self):
        print(f"{self.__student_id} - {self.__name} - {self.__dob}")
    

class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id
    
    def get_course_name(self):
        return self.__course_name
    
    def display(self):
        print(f"{self.__course_id} - {self.__course_name}")

    
class Std_mark_management:
    def __init__(self):
        self.__student = []
        self.__course = []
        self.__mark = {}

    def input_student(self):
        n = int(input("Enter number of student: "))
        for i in range(n):
            print(f"Student {i + 1}")
            sID = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Date of birthday: ")
            self.__student.append(Student(sID, name, dob))

    def input_course(self):
        n = int(input("Enter number of course: "))
        for i in range(n):
            print(f"Course {i + 1}")
            cID = input("Course ID: ")
            cName = input("Course name: ")
            self.__course.append(Course(cID, cName))

    def input_marks(self):
        print("Course: ")
        for c in self.__course:
            c.display()

        course_id = input("Choose course ID: ")

        for s in self.__student:
            mark = float(input(f"Enter mark for {s.get_name()}: "))
            self.__mark[(s.get_student_id(), course_id)] = mark

    def list_student(self):
        print("Student list: ")
        for s in self.__student:
            s.display()

    def list_course(self):
        print("Course list: ")
        for c in self.__course:
            c.display()

    def show_mark(self):
        course_id = input("Enter course ID: ")
        print("Marks: ")
        for s in self.__student:
            key = (s.get_student_id(), course_id)
            if key in self.__mark:
                print(s.get_name(), ":", self.__mark[key])
            else:
                print(s.get_name(), ": No mark")

    
def main():
    n = Std_mark_management()
    n.input_student()
    n.input_course()
    n.input_marks()
    n.list_student()
    n.list_course()
    n.show_mark()

main()