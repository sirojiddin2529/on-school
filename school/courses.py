def view_courses(courses_data: list) -> None:

    print("\nAvailable Courses:")
    for kurs in range(len(courses_data)):
        print("{}. {} (Duration: {}, Instructor: {})".format(kurs + 1,courses_data[kurs]['course_name'], courses_data[kurs]["duration"], courses_data[kurs]["instructor"]))
        