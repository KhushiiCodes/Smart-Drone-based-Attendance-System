import tkinter as tk
import subprocess

def run(script):
    root.iconify()
    subprocess.call(f"python {script}", shell=True)
    root.deiconify()

root = tk.Tk()
root.title("ESP32 Attendance System")
root.geometry("400x450")
root.configure(bg="#1A202C")

tk.Label(root, text="Smart Attendance System",
         bg="#1A202C", fg="white",
         font=("Arial", 16, "bold")).pack(pady=20)

buttons = [
    ("Register Student", "register.py"),
    ("Take Attendance", "attendance.py"),
    ("Show Students", "show_students.py"),
    ("Export Excel", "export_excel.py"),
    ("Delete Student", "delete_student.py"),
]

for text, script in buttons:
    tk.Button(root, text=text, width=25, height=2,
              command=lambda s=script: run(s)).pack(pady=8)

tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()