import subprocess

def change_password(username, current_password, new_password):
    subprocess.run(['net', 'user', username, current_password, new_password])

username = input("Enter your username: ")
current_password = input("Enter your current password: ")
new_password = input("Enter your new password: ")


change_password(username, current_password, new_password)
print("Password changed successfully.")
