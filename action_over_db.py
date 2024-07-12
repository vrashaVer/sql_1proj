import sqlite3

def open_connection():
    connection = sqlite3.connect('data.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return connection, cursor

def close_connection(connection,cursor):
    cursor.close()
    connection.close()

def create_student(name,age,major):
    connection, cursor = open_connection()
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",(name,age,major))
    connection.commit()
    close_connection(connection,cursor)

def create_course(course_name,instructor):
    connection, cursor = open_connection()
    cursor.execute("INSERT INTO courses (course_name,instructor) VALUES (?,?)",(course_name,instructor))
    connection.commit()
    close_connection(connection,cursor)

def view_students():
    connection, cursor = open_connection()
    students = cursor.execute("SELECT * FROM students").fetchall()
    close_connection(connection,cursor)
    return students

def view_courses():
    connection, cursor = open_connection()
    courses = cursor.execute("SELECT * FROM courses").fetchall()
    close_connection(connection,cursor)
    return courses

def register_student_to_course(student_id, course_id): 
    connection, cursor = open_connection()
    try:
        if not course_exists(course_id):
            raise ValueError(f"Курсу з ID {course_id} не існує.")
        
        if not student_exists(student_id):
            raise ValueError(f"Студента з ID {student_id} не існує.")
        
        cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        connection.commit()
        print("Студента успішно зареєстровано на курс")
    
    except Exception as e:
        print(f"Помилка при реєстрації студента на курс: {e}")
    
    finally:
        close_connection(connection, cursor)

def view_students_in_course(course_id):
    connection, cursor = open_connection()
    if course_exists(course_id):
        students = cursor.execute("SELECT students.id, students.name, students.age, students.major "
                "FROM students "
                "JOIN student_courses ON students.id = student_courses.student_id "
                "WHERE student_courses.course_id = ?",
                (course_id,)).fetchall() 
        close_connection(connection,cursor)
        return students

def student_exists(student_id):
    connection, cursor = open_connection()
    try:
        cursor.execute("SELECT 1 FROM students WHERE id = ?", (student_id,))
        exists = cursor.fetchone() is not None
        return exists
    finally:
        close_connection(connection, cursor)

def course_exists(course_id):
    connection, cursor = open_connection()
    try:
        cursor.execute("SELECT 1 FROM courses WHERE course_id = ?", (course_id,))
        exists = cursor.fetchone() is not None
        return exists
    finally:
        close_connection(connection, cursor)

    