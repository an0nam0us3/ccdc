import subprocess

def enable_windows_firewall():
    subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'on'])
    subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'firewallpolicy', 'blockinbound,allowoutbound'])


enable_windows_firewall()
print("Windows Firewall has been enabled with basic settings.")
