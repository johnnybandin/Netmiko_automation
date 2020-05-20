from pprint import pprint
def read_devices( devices_filename ):
    devices = {}
    with open( devices_filename ) as f:

        for device_line in f:

            device_info = device_line.strip().split(',')

            device = {
                'ipaddr': device_info[0],
                'type': device_info[1],
                'name': device_info[2]}

            devices[device['ipaddr']] = device
    print('\n----- devices ------------------------------------------------')
    pprint(devices)

    return devices
