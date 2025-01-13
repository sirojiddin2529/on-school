from school import students, courses, grades
import pprint
def main():
   
    student = {}

    students_data = []
    
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]

    grades_data = []

    while True:
        print("\n=== Welcome to On-School ===","1. Register","2. Login","3. Exit", sep="\n")
        choose_commond = int(input("Select an option: "))
        
        if choose_commond == 1:
            new_student = students.register_student(student, students_data)

            students_data.append(new_student)

            print("Registration successful! Welcome, {}".format(new_student["name"]), end="\n\n")
        elif choose_commond == 2:
            
            user = students.login_student(students_data)
            
            while user:
                
                print("\n--- Main Menu for Alice Smith --- \n1. View Available Courses\n2. Enroll in a Course\n3. View My Courses\n4. Check My Grades\n5. Logout\n6. exit")
                
                choose_commond_user = int(input("Choose an option: "))

                if choose_commond_user == 1:
                    courses.view_courses(courses_data)
                
                elif choose_commond_user == 2:
                    user['course'].append(students.enroll_in_course(courses_data, students_data, user['pas_log']['log']))
                
                elif choose_commond_user == 3:
                    courses.view_courses(user['course'])
                
                elif choose_commond_user == 4:
                    grades.check_grades(user, grades_data)
                
                elif choose_commond_user == 5:
                    break
                
                elif choose_commond_user == 6:
                    exit()
                else:
                    print("\nSiz mavjud bo`lmagan buyruq kiritdingiz iltimos tikshirib qaytadan kiriting! \n")
                  
        elif choose_commond == 3:
        
            print("Buyruqlar tugadi", sep="\n")
            exit()
        
        else: 
            
            print("Siz noto`gri buyrug` tanladingiz iltimos tikshirib qaytadan tiring: ", end="\n\n")

main()

if __name__ == "__main__":
    main()