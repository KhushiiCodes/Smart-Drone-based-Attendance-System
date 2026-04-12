import sqlite3

conn = sqlite3.connect("attendance.db")
c = conn.cursor()

c.execute("SELECT * FROM attendance")
rows = c.fetchall()

print("\n📋 Attendance Records:\n")

for row in rows:
    print(row)

conn.close()