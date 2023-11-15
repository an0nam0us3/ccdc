import subprocess

def disable_account(username):
    subprocess.run(['sudo', 'usermod', '-L', username])


username = input("Enter the username to disable: ")


disable_account(username)
print(f"The account '{username}' has been disabled.")

