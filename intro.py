import sqlite3

conn = sqlite3.connect('_students.db_')

c = conn.cursor()

# c.execute("""CREATE TABLE students (
#    StudentID interger,
#    Name text,
#    height real
#   )""")

c.execute("INSERT INTO students VALUES (45378, 'Baker', '5ft')")

c.execute("SELECT * FROM students WHERE Name='Baker'")

print(c.fetchone())


conn.commit()

conn.close()

