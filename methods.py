from list_array import List

def calculate_gpa():
    courses= List()
    lettergrade = List()
    numbers = List()
    gpa = List()
    grade_per = 0

    howmany = int(input("How many courses?: "))

    grade_conv = {
        "A+": (12, "90-100"), "A": (11, "85-89"), "A-": (10, "80-84"),
        "B+": (9, "77-79"), "B": (8, "73-76"), "B-": (7, "70-72"),
        "C+": (6, "67-69"), "C": (5, "63-66"), "C-": (4, "60-62"),
        "D+": (3, "57-59"), "D": (2, "53-56"), "D-": (1, "50-52"),
        "F": (0, "0-49")}

    for i in range(howmany):
        course_input= input("Enter a course code and name: ")
        courses.append(course_input)

        letter_input= input("Enter a letter grade for course: ").upper()
        lettergrade.append(letter_input)

        grade_point= grade_conv[letter_input][0]
        grade_range= grade_conv[letter_input][1]

        gpa.append(grade_point)
        numbers.append(grade_range)

    print()
    print(f"{'Course Name':^15}{'Letter Grade':^25}{'Number Grade':^20}{'GP':^5}")

    for x in range(howmany):
        print(f"{courses[x]:^15}{lettergrade[x]:^25}{numbers[x]:^20}{gpa[x]:^5}")
        print()
        grade_per+= gpa[x]

    average= (grade_per / howmany)
    print(f"Your GPA is: {average}")
