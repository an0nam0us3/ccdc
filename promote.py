import subprocess

def promote_to_admin(username):
    subprocess.run(['net', 'localgroup', 'Administrators', username, '/add'])


username = input("Enter username to promote to admin: ")


promote_to_admin(username)
print(f"The user '{username}' has been promoted to admin.")
