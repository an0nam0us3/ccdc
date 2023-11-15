import subprocess

def run_program(filename):
    subprocess.run(["python",filename])
   

def display_menu_linux():
    print("1. Run iptables")  
    print("2. Make a usr no pass")  
    print("3. Clear cron")  
    print("4. Change admin password")
    print("5. Update")
    print("6. Remove a user from sudo")  
    print("8. Exit")

def display_menu_windows():
    print("1. Change admin password")  
    print("2. Create new user (make a duck)")  
    print("3. Promote user to admin")
    print("4. Disable SAM accounts")
    print("5. Update")
    print("6. Open Windows Firewall")
    print("7. Run security lockdown")
    print("8. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("number between 1 and 8.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

def main():
    os_type = input("Enter 'l' for Linux or 'w' for Windows: ")
    if os_type == 'l':
        file_extension = '.py'
        display_menu = display_menu_linux
    elif os_type == 'w':
        file_extension = '.py'
        display_menu = display_menu_windows
    else:
        print("Invalid input. Exiting program.")
        return

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 8:
            print("Exiting program.")
            break

        if os_type == 'l':
          
            if choice == 1:
                filename = "iptable.py"  
            elif choice == 2:
                filename = "addusr.py"  
            elif choice == 3:
                filename = "cron_task.py"
            elif choice == 4:
                filename = "chgepass.py"
            elif choice == 5:
                filename = "update.py"
            elif choice == 6:
                filename = "deleteadmin.py"
            elif choice == 7:
                filename = "disable.py"
        else:
           
            if choice == 1:
                filename = "wpasswd.py"  
            elif choice == 2:
                filename = "wRubberDuck.py"  
            elif choice == 3:
                filename = "promote.py"  
            elif choice == 4:
                filename = "disableacct.py"
            elif choice == 5:
                filename = "wupdate.py"
            elif choice == 6:
                filename = "wfirewall.py"
            elif choice == 7:
                filename = "security.py"
            

        if filename:
            run_program(filename)
        else:
            print("Invalid selection. File does not exist.")

if __name__ == '__main__':
    main()
