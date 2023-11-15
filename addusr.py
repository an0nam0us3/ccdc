import subprocess

def create_user(username):
    subprocess.run(['sudo', 'useradd', username])

username = input("Enter the username for the new user: ")
create_user(username)
print(f"User '{username}' has been created.")

