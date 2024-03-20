import psycopg2

def connect():
    try:
        return psycopg2.connect(
            dbname="Students",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)

def getAllStudents():
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students;")
            rows = cur.fetchall()
            print("All students:")
            for row in rows:
                print(row)
    else:
        print("Connection to database failed.")

def execute_sql(sql, values=None):
    conn = connect()
    if conn:
        with conn.cursor() as cur:
            cur.execute(sql, values)
            conn.commit()
    else:
        print("Connection to database failed.")

def addStudent(first_name, last_name, email, enrollment_date):
    sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
    values = (first_name, last_name, email, enrollment_date)
    execute_sql(sql, values)
    print("Student added successfully.")

def updateStudentEmail(student_id, new_email):
    sql = "UPDATE students SET email = %s WHERE student_id = %s;"
    values = (new_email, student_id)
    execute_sql(sql, values)
    print("Email updated successfully.")

def deleteStudent(student_id):
    sql = "DELETE FROM students WHERE student_id = %s;"
    values = (student_id,)
    execute_sql(sql, values)
    print("Student deleted successfully.")

if __name__ == "__main__":
    getAllStudents()
    #addStudent("Billy", "Bob", "alice@example.com", "2024-03-19")
    #updateStudentEmail(9, "john.doe.updated@example.com")
    #deleteStudent(2)
