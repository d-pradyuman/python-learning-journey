def get_student_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = int(input("Enter your marks: "))

    return name, age, marks


def calculate_percentage(marks):
    return marks / 500 * 100


def calculate_grade(percentage):
    if percentage >= 95:
        return "A+"
    elif percentage >= 90:
        return "A"
    elif percentage >= 85:
        return "B+"
    elif percentage >= 80:
        return "B"
    elif percentage >= 75:
        return "C+"
    elif percentage >= 70:
        return "C"
    elif percentage >= 65:
        return "D+"
    elif percentage >= 60:
        return "D"
    elif percentage >= 55:
        return "E+"
    elif percentage >= 50:
        return "E"
    else:
        return "F"


def check_result(percentage):
    return percentage >= 33


def display_result(name, age, marks, percentage, grade, result):
    print("\n--- Student Result ---")
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks, "/ 500")
    print("Percentage:", percentage)
    print("Grade:", grade)

    if result:
        print("Result: Pass")
    else:
        print("Result: Fail")


name, age, marks = get_student_data()

percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)
result = check_result(percentage)

display_result(name, age, marks, percentage, grade, result)