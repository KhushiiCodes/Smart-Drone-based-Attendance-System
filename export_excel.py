import sqlite3
import pandas as pd

conn = sqlite3.connect("attendance.db")

df = pd.read_sql_query("SELECT * FROM attendance", conn)
df.to_excel("attendance.xlsx", index=False)

print("Exported ✅")

conn.close()