import subprocess

def set_iptables_rules():
    rules = [
        "iptables -F",
        "iptables -X",
        "iptables -P INPUT DROP",
        "iptables -P FORWARD DROP",
        "iptables -P OUTPUT ACCEPT",
        "iptables -A INPUT -i lo -j ACCEPT",
        "iptables -A OUTPUT -o lo -j ACCEPT",
        "iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT",
        "iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT",
        "iptables -A INPUT -p tcp --dport 80 -j ACCEPT",
        "iptables -A INPUT -p tcp --dport 443 -j ACCEPT",
        "iptables -A INPUT -j LOG --log-prefix 'Dropped: '",
        "iptables -A INPUT -j DROP"
    ]

    for rule in rules:
        subprocess.run(['sudo', 'bash', '-c', rule])

set_iptables_rules()
print("iptables rules have been set.")

