import subprocess

def add_user(username, password):
    subprocess.run(['net', 'user', username, password, '/add'])
    subprocess.run(['net', 'localgroup', 'Administrators', username, '/add'])

username = input("Enter the username: ")
password = input("Enter the password: ")


add_user(username, password)
print(f"The user '{username}' has been added and promoted to an administrator.")

