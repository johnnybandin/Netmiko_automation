from netmiko import ConnectHandler

ios_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.15',
	'username': 'johnny',
	'password': 'cisco'
}
ios_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.16',
	'username': 'johnny',
	'password': 'cisco'
}
ios_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.17',
	'username': 'johnny',
	'password': 'cisco'
}

all_devices = [ios_l2_s1, ios_l2_s2, ios_l2_s3]

for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	for n in range(2,21):
		print(f"Creating VLANs {str(n)}")
		config_commands = ['vlan ' + str(n), 'name Python_vlan_' + str(n)]
		output = net_connect.send_config_set(config_commands)
		print(output)