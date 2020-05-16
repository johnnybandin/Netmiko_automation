from netmiko import ConnectHandler

iosv_l2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.15',
	'username': 'johnny',
	'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)
