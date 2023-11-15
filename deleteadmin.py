import subprocess

def remove_from_sudo(username):
    subprocess.run(['sudo', 'deluser', username, 'sudo'])

username = input("Enter the username to remove from sudo: ")

remove_from_sudo(username)
print(f"The user '{username}' has been removed from the sudo group.")

