import time
import logging
import diarymanager


def print_options():
    logging.info(f"Choose an action:")
    logging.info("1. Print schools")
    logging.info("2. Print courses in school")
    logging.info("3. Print grades in course")
    logging.info("4. Add school")
    logging.info("5. Add course")
    logging.info("6. Add grade")
    logging.info("7. Get mean")
    logging.info("8. Exit diary")


def print_schools_option():
    for school in filter(None, diarymanager.get_diary_from_file()):
        logging.info(school)


def print_courses_option():
    diary = diarymanager.get_diary_from_file()
    school = input('School name: ')

    logging.info(diarymanager.get_courses(diary, school))


def print_grades_option():
    diary = diarymanager.get_diary_from_file()
    school = input('School name: ')
    course = input('Course name: ') 

    logging.info(diarymanager.get_grades(diary, school, course))


def add_school_option():
    diary = diarymanager.get_diary_from_file()
    diary[input("School name: ")] = {}
    diarymanager.save_diary_in_file(diary)
    time.sleep(0.2)
    logging.info("\nSchool was added succesfully!")


def add_course_option():
    diary = diarymanager.get_diary_from_file()
    try:
        diary[input("School name: ")][input("Course name: ")] = {}
        diarymanager.save_diary_in_file(diary)
        time.sleep(0.2)
        logging.info("\nCourse was added succesfully!")
    except KeyError:
        logging.error("There is no school like that")


def add_grade_option():
    diary = diarymanager.get_diary_from_file()
    school = input("School name: ")
    course = input("Course name: ")
    student = input("Student name: ")
    try:
        grade = int(input("Grade: "))
        diary[school][course][student] = grade
        diarymanager.save_diary_in_file(diary)
        time.sleep(0.2)
        logging.info("\nGrade was added succesfully!")
    except KeyError:
        logging.error("There is no school or course like that")
    except ValueError:
        logging.error("Grade is NAN")


def get_mean_option():
    logging.info("Get mean grades across: ")
    logging.info("1. Students in courses")
    logging.info("2. Courses in school")
    logging.info("3. All courses for a student")
    try:
        action = int(input("Action: "))
    except ValueError:
        logging.error("Action is NAN")

    if action == 1:
        school = input("School name: ")
        course = input("Course name: ")
        logging.info(diarymanager.mean_in_course(
                     diarymanager.get_diary_from_file(),
                     school,
                     course))
    elif action == 2:
        school = input("School name: ")
        logging.info(diarymanager.mean_in_school(
                     diarymanager.get_diary_from_file(),
                     school))
    elif action == 3:
        student = input("Student name: ")
        logging.info(diarymanager.mean_for_student(
                     diarymanager.get_diary_from_file(),
                     student))