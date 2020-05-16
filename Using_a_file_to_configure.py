from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

# Set login parameters for devices
ios_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.16',
	'username': 'johnny',
	'password': password
} 
ios_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.17',
	'username': 'johnny',
	'password': password
} 
# Open text file with device configuration
filename = 'Cisco_Switch_design.txt'
with open(filename) as f:
	# Create variable for all lines of config file
	lines = f.read().splitlines()
print(lines)

# Create variable for all devices you want to configure
all_devices = [ios_l2_s2, ios_l2_s3]


for device in all_devices:
	print(f'Connecting to {device}')
	net_connect = ConnectHandler(**device)
	output = net_connect.send_config_set(lines)
	print(output)
