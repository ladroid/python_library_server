import psycopg2
import datetime

def connetion_db():
    try:
        conn = psycopg2.connect("dbname='jdbcproj' user='postgres' host='localhost' password='1'")
        return conn
    except:
        print("I am unable to connect to the database")

def get_book():
    list_book = []
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        for r in cur:
            #print(r)
            #return r
            list_book.append(r)
        return list_book
    except:
        print("Unable to connect to the db")

def get_authorz():
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("SELECT * FROM authorz")
        for authz in cur:
            print(authz)
    except:
        print("Unable to connect to the db")

def get_students():
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons")
        for authz in cur:
            print(authz)
    except:
        print("Unable to connect to the db")

def get_borrows():
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("SELECT * FROM borrows")
        for borrows in cur:
            print(borrows)
    except:
        print("Unable to connect to the db")

def get_type():
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("SELECT * FROM types")
        for authz in cur:
            print(authz)
    except:
        print("Unable to connect to the db")

def insert_authorz(id_, name, surname):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("INSERT INTO authorz (authorId, name, surname) VALUES (%s, %s, %s)",
                    (id_, name, surname))
        conn.commit()
    except:
        print("Unable to connect to the db")

def insert_book(bookId, name, pagecount, point, authorId, typeId):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("INSERT INTO books (bookId, name, pagecount, point, authorId, typeId) VALUES (%s, %s, %s, %s, %s, %s)",
                    (bookId, name, pagecount, point, authorId, typeId))
        conn.commit()
    except:
        print("Unable to connect to the db")

def insert_borrows(borrowId, studentId, bookId, takenDate, broughtDate):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("INSERT INTO borrows (borrowId, studentId, bookId, takenDate, broughtDate) VALUES (%s, %s, %s, %s, %s)",
                    (borrowId, studentId, bookId, takenDate, broughtDate))
        conn.commit()
    except:
        print("Unable to connect to the db")

def insert_students(studentId, name, surname, email, passwords, birthdate, gender, job, point, phone_number):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("INSERT INTO persons (personId, name, surname, email, passwords, birthdate, gender, job, point, phone_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (studentId, name, surname, email, passwords, birthdate, gender, job, point, phone_number))
        conn.commit()
    except:
        print("Unable to connect to the db")

def remove_student():
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE personId = 21")
        conn.commit()
    except:
        print("Unable to connect to the db")

def check_info_student(email, password):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons WHERE email = %s AND passwords = %s", (email, password))
        for student in cur:
            print(student)
            if student[3] == email:
                return True
            else:
                return False
    except:
        print("Unable to connect to the db")

def get_info_student(email, password):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons WHERE email = %s AND passwords = %s", (email, password))
        for student in cur:
            print(student)
            return student[1], student[2], student[3], student[9]
    except:
        print("Unable to connect to the db")

def get_book_name():
    list_book = []
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute("SELECT name FROM books")
        for r in cur:
            list_book.append(r)
        return list_book
    except:
        print("Unable to connect to the db")

def taken_book(email):
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute("""SELECT books.name, persons.point, books.point FROM books 
                    INNER JOIN persons ON books.point = persons.point 
                    WHERE persons.email = %s""", (email,))
        for stud in cur:
            return stud[0]
    except:
        print("Unable to connect to the db")

def delete_author(name):
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute("DELETE FROM authorz WHERE surname = %s", (name,))
        conn.commit()
    except:
        print("Unable to connect to the db")

def delete_book(name):
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE name = %s", (name,))
        conn.commit()
    except:
        print("Unable to connect to the db")

def get_borrows_student():
    list_borrows_student = []
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute('''SELECT persons.name, persons.surname, persons.email, persons.phone_number, borrows.takenDate, books.name FROM borrows
                    INNER JOIN persons
                    ON borrows.personId = persons.personId
                    INNER JOIN books
                    ON borrows.bookId = books.bookId''')
        for r in cur:
            list_borrows_student.append(r)
        return list_borrows_student
    except:
        print("Unable to connect to the db")

def search_student(email):
    try:
        conn = connetion_db()
        print("Connected!")
        cur = conn.cursor()
        cur.execute('''SELECT persons.name, persons.surname, persons.email, persons.phone_number, borrows.takenDate, books.name FROM borrows
                    INNER JOIN persons
                    ON borrows.personId = persons.personId
                    INNER JOIN books
                    ON borrows.bookId = books.bookId 
                    WHERE persons.email = %s''', (email, ))
        for students in cur:
            return students
    except:
        print("Unable to connect to the db")

def get_time_take(email):
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute('''SELECT borrows.takenDate FROM borrows
                    INNER JOIN persons
                    ON borrows.personId = persons.personId
                    WHERE persons.email = %s''', (email, ))
        for t in cur:
            for tt in t:
                return tt
    except:
        print("Unable to connect to the db")

def get_free_books():
    list_free_books = []
    try:
        conn = connetion_db()
        print("Connected")
        cur = conn.cursor()
        cur.execute('''SELECT books.bookid FROM books
                       FULL OUTER JOIN persons
                       ON books.point = persons.point
                       WHERE books.point IS NULL OR persons.point IS NULL''')
        for free_books in cur:
            for i in free_books:
                list_free_books.append(i)
        return list_free_books
    except:
        print("Unable to connect to the db")

#insert_students(21, 'Alberto', 'Qasterro', 'albert@yahoo.mail.com', 'alberto', datetime.date(1998, 3, 12), 'M', '11C', 93, '+13224567890')
#remove_student()
#get_students()
#print(get_book())
#get_type()
#print(get_info_student("carteradams@gmail.com", "cartenadams"))
#get_authorz()
#print(get_book_name())
#print(taken_book("carteradams@gmail.com"))
#print(get_borrows_student())
print(search_student("hazgreen@gmail.com"))
get_time_take("hazgreen@gmail.com")
print(get_free_books())