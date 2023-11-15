import subprocess

def clear_cron_tasks():

    users = subprocess.check_output(['cut', '-d:', '-f1', '/etc/passwd']).decode().splitlines()


    for user in users:
        subprocess.run(['sudo', '-u', user, 'crontab', '-r'])


clear_cron_tasks()
print("Cron tasks cleared for all users.")

