from read_device_creds import read_device_creds
from read_devices import read_devices
from config_worker import config_worker
from simplecrypt import encrypt, decrypt
from netmiko import ConnectHandler
from pprint import pprint
import json
from time import time
from multiprocessing.dummy import Pool as ThreadPool

devices = read_devices( 'devices-file' )
creds = read_device_creds( 'encrypted-device-creds', 'cisco')

num_threads_str = input( '\nNumber of threads (5) : ' ) or '5'
num_threads     = int( num_threads_str )
#---- Create list for passing to config worker
config_params_list = []
for ipaddr,device in devices.items():
    config_params_list.append( ( device, creds[ipaddr] ) )
print('\n---- Create threadpool, launching get config threads\n')
threads = ThreadPool( num_threads )
results = threads.map( config_worker, config_params_list )

threads.close()
threads.join()

print('\n---- End get config threadpool-----')

