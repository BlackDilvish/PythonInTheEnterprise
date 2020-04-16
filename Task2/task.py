import time
import logging
import consoleinfo
import diarymanager

actions = {
    1: consoleinfo.print_schools_option,
    2: consoleinfo.print_courses_option,
    3: consoleinfo.print_grades_option,
    4: consoleinfo.add_school_option,
    5: consoleinfo.add_course_option,
    6: consoleinfo.add_grade_option,
    7: consoleinfo.get_mean_option,
    8: exit
    }


def set_logger():
    a_logger = logging.getLogger()
    a_logger.setLevel(logging.NOTSET)
    output_file_handler = logging.FileHandler("output.log")
    console_handler = logging.StreamHandler()
    a_logger.addHandler(output_file_handler)
    a_logger.addHandler(console_handler)

if __name__ == '__main__':
    set_logger()
    while True:
        consoleinfo.print_options()

        try:
            action = int(input("Action: "))
        except ValueError:
            logging.error("Undefined action")

        logging.info("==================")
        if action in actions:
            actions[action]()
        else:
            logging.error("Out of range")

        logging.info("==================")
        time.sleep(0.5)    