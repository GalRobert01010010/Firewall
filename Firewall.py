import random   #we import a random module (to generate random IP addresses)

def generates_random_ip():   #generates a random IP that is the source IP
    return f"192.168.1.{random.randint(0, 20)}"   

def check_firewall_rules(ip, rules):   #takes the IP address and the dictionary of rules
    for rule_ip, action in rules.items():
        if ip == rule_ip:   #checks if the address matckes any of the rules
            return action   #the action is to block the IP that matched the one in the blocklist
    return "allow"

def main():   #defining the main function that consists of two parts
    firewall_rules = {   #is a defined dictionary
        "192.168.1.1": "block",   #the IP addressed we have decided not to allow on our internal network
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }
    for _ in range(12):   # loop that simulates random oncoming traffic
        ip_address = generates_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)   #to distinguish the actions taken against an incident
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")
        #prints to the terminal the IP of the analised pack, the action taken against it and and its unique identifying number

if __name__ == "__main__":   #the main guard (ensures that when the script is executed the main function is called)
    main()