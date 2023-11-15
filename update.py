import subprocess

def check_for_updates():
    subprocess.run(['sudo', 'apt', 'update'])
def perform_updates():
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
check_for_updates()
response = input("Updates are available. Do you want to proceed? (y/n): ")
if response.lower() == 'y':

    perform_updates()
    print("updates have been installed.")
else:
    print("Update canceled.")
