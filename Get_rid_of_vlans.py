from netmiko import ConnectHandler

iosv_l2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.15',
	'username': 'johnny',
	'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
for n in range(2,21):
	print(f"Deleting VLAN {str(n)}")
	config_commands = ['no vlan ' + str(n)]
	output = net_connect.send_config_set(config_commands)
	print(output)