import subprocess

def change_password(username, new_password):
    subprocess.run(['sudo', 'passwd', username], input=new_password.encode())

# Prompt for username and new password
username = input("Enter the username: ")
new_password = input("Enter the new password: ")

# Change the user's password
change_password(username, new_password)
print("Password has been changed successfully.")
