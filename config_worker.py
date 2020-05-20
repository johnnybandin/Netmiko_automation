from simplecrypt import encrypt, decrypt
from pprint import pprint
from netmiko import ConnectHandler
import json
from time import time

def config_worker( device_and_creds ):
    # For threadpool library we had to pass only one argument, so extract the two
    # pieces (device and creds) out of the one tuple passed
    device = device_and_creds[0]
    creds = device_and_creds[1]

    # ------ Connect to the devices----
    if device['type'] == 'junos-srx': device_type = 'juniper'
    elif device['type'] == 'cisco-ios': device_type = 'cisco_ios'
    elif device['type'] == 'cisco-xr': device_type = 'cisco_xr'
    else:                              device_type = 'cisco_ios'

    print(f'----- Connecting to device {0}, username={1}, password={2}'.format( device['ipaddr'], creds[1], creds[2]))

    # -------- Connect to the device-----
    session = ConnectHandler( device_type=device_type, ip=device['ipaddr'], username=creds[1], password=creds[2] )

    if device_type == 'juniper':
        #----- Use CLI command to get configuration data from device
        print(f"------Getting configuration from device")
        session.send_command('configure terminal')
        config_data = session.send_command('show configuration')
    if device_type == 'cisco_ios':
        #----- Use CLI command to get configuration data from device
        print('----- Getting configuration from device')
        config_data = session.send_command('show run')
    if device_type == 'cisco_xr':
        #----- Use CLI command to get configuration data from device
        print('----- Getting configuration data from device')
        config_data = session.send_command('show configuration running-config')
    
    config_filename = f"config-{device['ipaddr']}"

    print(f'-------------- Writing configuration: {config_filename} ')
    with open( config_filename, 'w') as f:
        f.write(config_data)
    
    session.disconnect()

    return