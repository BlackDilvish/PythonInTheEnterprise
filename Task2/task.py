
class Diary:
    def __init__(self):
        self.schools = []

    def add_school(self):
        inp = input("School name: ")
        self.schools.append(School(inp))


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}
        self.attendances = {}

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self):
        inp = input("Student name: ")
        self.students.append(Student(inp))
    
    def give_grade(self, student_name, class_name):
        for student in self.students:
            if student.name == student_name:
                try:
                    student.grades[class_name] = float(input("Give grade: "))
                    return 1
                except KeyboardInterrupt:
                    pass
            else:
                return 0

    def give_attendance(self, student_name, class_name):
        for student in self.students:
            if student.name == student_name:
                student.attendances[class_name] += 1
                return 1
            else:
                return 0

class InfoWriter:
    def print_options(self):
        print(f"Choose an action:")
        print("1. Add a school to diary")
        print("2. Add a student to school")
        print("3. Add a grade to student")
        print("4. Add a attendance to student")
        print("5. Print schools")
        print("6. Exit diary")

    def handle_option(self):
        try:
            return int(input("Action: "))
        except KeyboardInterrupt:
            pass

    def print_schools(self, schools):
        for school in schools:
            print(f"{school.name}\n")

if __name__ == '__main__':
    
    diary = Diary()
    info = InfoWriter()

    while True:
        info.print_options()

        choice = info.handle_option()

        if choice == 1:
            diary.add_school()
        elif choice == 2:
            diary.schools[0].add_student()
        elif choice == 3:
            diary.schools[0].give_grade(input("Student name: "), input("Class name: "))
        elif choice == 4:
            diary.schools[0].give_attendance(input("Student name: "), input("Class name: "))
        elif choice == 5:
            for school in diary.schools:
                print(f"{school.name}\n")
        elif choice == 6:
            break
            
