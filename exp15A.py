import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

# Drop table if it exists (to reset schema and avoid column mismatch)
cursor.execute('DROP TABLE IF EXISTS student_record')

# Create updated table with studentId to support multiple subjects per student
cursor.execute('''CREATE TABLE student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    studentId INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

conn.commit()

# Insert multiple subjects per student
student_record = [
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'PWP', 95),
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'DBMS', 88),
    (92301733016, 'ASHUTOSH KUMAR SINGH', 'OS', 91),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI', 'PWP', 85),
    (92301733017, 'HARSH VISHALBHAI TRIVEDI', 'DBMS', 80),
    (92301733027, 'VIRAJ PRAKASHBHAI VAGHASIYA', 'PWP', 90),
    (92301733046, 'SHIVAM ATULKUMAR BHATT', 'PWP', 93),
    (92301733058, 'DEVENDRASINH DOLATSINH JADEJA', 'PWP', 75)
]

cursor.executemany('''INSERT INTO student_record (studentId, name, Subject, Mark)
                      VALUES (?, ?, ?, ?)''', student_record)

conn.commit()

# Display all records
cursor.execute('SELECT studentId, name, Subject, Mark FROM student_record')
rows = cursor.fetchall()
print("All Student Records:")
for row in rows:
    print(row)

# Students with marks greater than 90
cursor.execute('SELECT name, Subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()
print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Update a mark
cursor.execute('''UPDATE student_record SET Mark = 98 
                  WHERE name = 'ASHUTOSH KUMAR SINGH' AND Subject = 'PWP' ''')
conn.commit()

cursor.execute('SELECT name, Mark FROM student_record WHERE name = "ASHUTOSH KUMAR SINGH" AND Subject = "PWP"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark for {updated_mark[0]} (PWP): {updated_mark[1]}")

# Delete a student record
cursor.execute('''DELETE FROM student_record WHERE name = 'DEVENDRASINH DOLATSINH JADEJA' ''')
conn.commit()

cursor.execute('SELECT * FROM student_record WHERE name = "DEVENDRASINH DOLATSINH JADEJA"')
deleted_name = cursor.fetchone()
if deleted_name is None:
    print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")

# Average mark
cursor.execute('''SELECT AVG(Mark) FROM student_record''')
avg_mark = cursor.fetchone()[0]
print(f"\nThe average mark of students is: {avg_mark:.2f}")

conn.close()