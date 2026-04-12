import sqlite3

def create_databases():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students (
                    id TEXT PRIMARY KEY,
                    name TEXT
                )""")
    conn.commit()
    conn.close()

    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS attendance (
                    id TEXT,
                    name TEXT,
                    date TEXT,
                    time TEXT
                )""")
    conn.commit()
    conn.close()

def add_student(id, name):
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO students VALUES (?,?)", (id, name))
    except:
        print("Student already exists")
    conn.commit()
    conn.close()

def mark_attendance(id, name, date, time):
    conn = sqlite3.connect("attendance.db")
    c = conn.cursor()

    c.execute("SELECT * FROM attendance WHERE id=? AND date=?", (id, date))
    if not c.fetchone():
        c.execute("INSERT INTO attendance VALUES (?,?,?,?)",
                  (id, name, date, time))
        conn.commit()

    conn.close()