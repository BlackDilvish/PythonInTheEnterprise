import json

data_file = 'data.json'


def get_diary_from_file(filename=data_file):
    with open(data_file, 'r') as f:
        diary = json.loads(f.read())
    return diary


def save_diary_in_file(data, filename=data_file):
    with open(filename, 'w') as f:
            f.write(json.dumps(data))


def get_courses(diary, school):
    return [c for c in diary[school] if school in diary]


def get_grades(diary, school, course):
    return [f"{s} : {diary[school][course][s]}"
            for s in diary[school][course]
            if school in diary and course in diary[school]]


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


def mean_in_course(diary, school, course):
    try:
        return mean([diary[school][course][s] 
                    for s in diary[school][course]
                    if school in diary and course in diary[school]])
    except KeyError:
        pass


def mean_in_school(diary, school):
    grades = []
    for course in diary[school]:
        for grade in diary[school][course]:
            grades.append(diary[school][course][grade])
    return mean(grades)


def mean_for_student(diary, student):
    grades = []
    for school in diary:
        grades += [diary[school][course][student]
                   for course in diary[school]
                   if student in diary[school][course]]
    return mean(grades)
