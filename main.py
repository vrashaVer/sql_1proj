import sqlite3
from action_over_db import create_course,create_student,view_courses,view_students,view_students_in_course,register_student_to_course,student_exists,course_exists


if __name__ == "__main__":
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    with open('create_db.sql', encoding='utf-8') as file:
        cursor.executescript(file.read())
        connection.commit()

    cursor.close()
    connection.close
    
    while True:
        print("////////////////////////////////////////////////////////////")
        print("\n1. Додати нового студента")
        print("2. Додати новий курс")
        print("3. Показати список студентів")
        print("4. Показати список курсів")
        print("5. Зареєструвати студента на курс")
        print("6. Показати студентів на конкретному курсі")
        print("7. Вийти")
        print("\n////////////////////////////////////////////////////////////")
        choice = input("Оберіть опцію (1-7): ")

    
        if choice == "1":
            name = input("Введіть ім'я: ")
            while True:
                try:
                    age = int(input("Введіть вік: "))
                    break
                except ValueError:
                    print("Будь ласка, введіть ціле число.")
            major = input("Введіть спеціальність: ")
            create_student(name, age, major)
            print("Студента успішно додано")
            
        elif choice == "2":
            course_name = input("Введіть назву курсу: ")
            instructor = input("Введіть ім'я інстуктора: ")
            create_course(course_name,instructor)
            print("Курс успішно додан")
        
        elif choice == "3":
            n = 0
            print("Список студентів:")
            for student in view_students():
                n += 1
                print(f"{n}. {student['name']}")
        
        elif choice == "4":
            n = 0
            print("Список курсів:")
            for course in view_courses():
                n += 1
                print(f"{n}. {course['course_name']}")

        elif choice == "5":
            while True:
                try:
                    student_id = int(input("Введіть ID студента: "))
                    break
                except ValueError:
                    print("Будь ласка, введіть ціле число.")

            while True:
                try:
                    course_id = int(input("Введіть ID курсу: "))
                    break
                except ValueError:
                    print("Будь ласка, введіть ціле число.")

            try:
                register_student_to_course(student_id, course_id)
            except Exception as e:
                print(e)

        elif choice == "6":
            while True:
                try:
                    course_id = int(input("Введіть ID курсу: "))
                    students = view_students_in_course(course_id)
                    if students is not None:
                        print(f"Студенти на курсі з ID {course_id}:")
                        for student in students:
                            print(f"{student['id']}. {student['name']} ({student['age']} років, {student['major']})")
                    else:
                        print(f"На курсі з ID {course_id} ще немає зареєстрованих студентів.")
                    break
                except ValueError:
                    print("Будь ласка, введіть ціле число.")
                except Exception as e:
                    print(f"Сталась помилка: {e}")
                
        elif choice == "7":
            break

        else:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
