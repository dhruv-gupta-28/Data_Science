# Task 13: Attendance System
# Goal:
# - Store login time
# - Store logout time
# - Calculate total session duration

from datetime import datetime

# Dictionary to store attendance records
attendance_records = {}

print("📋 Attendance System")
print("-" * 40)

while True:
    print("\n1. Login")
    print("2. Logout")
    print("3. View Records")
    print("4. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        name = input("Enter your name: ").strip()
        if name in attendance_records and attendance_records[name]['logout_time'] is None:
            print("You are already logged in!")
        else:
            login_time = datetime.now()
            attendance_records[name] = {
                'login_time': login_time,
                'logout_time': None,
                'session_duration': None
            }
            print(f"✅ {name} logged in at {login_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    elif choice == '2':
        name = input("Enter your name: ").strip()
        if name not in attendance_records:
            print("No login record found!")
        elif attendance_records[name]['logout_time'] is not None:
            print("You are already logged out!")
        else:
            logout_time = datetime.now()
            login_time = attendance_records[name]['login_time']
            session_duration = logout_time - login_time
            
            attendance_records[name]['logout_time'] = logout_time
            attendance_records[name]['session_duration'] = session_duration
            
            hours = int(session_duration.total_seconds() // 3600)
            minutes = int((session_duration.total_seconds() % 3600) // 60)
            seconds = int(session_duration.total_seconds() % 60)
            
            print(f"✅ {name} logged out at {logout_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"⏱️  Session duration: {hours}h {minutes}m {seconds}s")
    
    elif choice == '3':
        if not attendance_records:
            print("No records found!")
        else:
            print("\n📊 Attendance Records:")
            print("-" * 60)
            for name, record in attendance_records.items():
                print(f"\nName: {name}")
                print(f"Login: {record['login_time'].strftime('%Y-%m-%d %H:%M:%S')}")
                if record['logout_time']:
                    print(f"Logout: {record['logout_time'].strftime('%Y-%m-%d %H:%M:%S')}")
                    duration = record['session_duration']
                    hours = int(duration.total_seconds() // 3600)
                    minutes = int((duration.total_seconds() % 3600) // 60)
                    seconds = int(duration.total_seconds() % 60)
                    print(f"Duration: {hours}h {minutes}m {seconds}s")
                else:
                    print("Status: Currently logged in")
                print("-" * 60)
    
    elif choice == '4':
        print("Thank you for using Attendance System!")
        break
    
    else:
        print("Invalid choice! Please try again.")
