import subprocess

def perform_updates():
    subprocess.run(['cmd', '/c', 'start', 'ms-settings:windowsupdate-action'])


perform_updates()
print("System updates are being performed. Please wait...")


