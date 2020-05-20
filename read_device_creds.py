from simplecrypt import encrypt, decrypt
from pprint import pprint
import json

def read_device_creds( device_creds_filename, key ):

    print('\n... getting credentials...\n')
    with open( device_creds_filename, 'rb') as f:
        device_creds_json = decrypt( key, f.read() )

    device_creds_list = json.loads( device_creds_json.decode('utf-8'))
    pprint( device_creds_list )

    print('\n----- device_creds ----------------------------------')

    device_creds = { dev[0]:dev for dev in device_creds_list }
    pprint( device_creds )

    return device_creds

