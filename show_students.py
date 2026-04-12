import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()

c.execute("SELECT * FROM students")

print("\nID\tName")
print("--------------")

for row in c.fetchall():
    print(row[0], "\t", row[1])

conn.close()