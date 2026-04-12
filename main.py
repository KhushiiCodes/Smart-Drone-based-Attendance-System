from database import create_databases

create_databases()

while True:
    print("\n1. Register Student")
    print("2. Train Model")
    print("3. Take Attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        import register
    elif choice == '2':
        import train
    elif choice == '3':
        import attendance
    elif choice == '4':
        break
    else:
        print("Invalid Choice")