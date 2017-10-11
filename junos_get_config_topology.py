from napalm_base import get_network_driver
from yaml import load
import os

# make sure backup directory exists
cwd = os.getcwd()
backup_directory = os.path.dirname(cwd + "/backup/")
if not os.path.exists(backup_directory):
     os.makedirs(backup_directory)

# getting inventory in a python data structure. 
inventory_f=open('python_inventory.yml', 'r')
inventory_s=inventory_f.read()
inventory_f.close()
python_inventory=load(inventory_s)

# get devices running configuration and save it in backup directory
junos_driver = get_network_driver('junos')
for device_item in python_inventory:
    junos_device = junos_driver(hostname=python_inventory[device_item]['ip'], username='pytraining', password='Poclab123', optional_args={'port': 830})
    junos_device.open()
#   type junos_device.get_config()
#   print junos_device.get_config()['running']
    conf=open(backup_directory + '/' + device_item + '_config.txt','w')
    conf.write(junos_device.get_config()['running'])
    conf.close()
    junos_device.close()


'''
# python ./junos_get_config_topology.py
# ls backup/
ex4200_12_config.txt  ex4200_7_config.txt  ex4200_8_config.txt
'''
