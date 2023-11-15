import subprocess

def disable_account(username):
    subprocess.run(['net', 'user', username, '/active:no'])

username = input("Enter username to disable: ")

disable_account(username)
print(f"The account '{username}' has been disabled.")
