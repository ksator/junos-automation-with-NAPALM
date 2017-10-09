from napalm_base import get_network_driver
from pprint import pprint
from json import dumps


junos_driver = get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

with junos_driver(**junos_device) as junos:
    print('-'*60)
    pprint(junos.get_interfaces())
    print('-'*60)
    print dumps(junos.get_interfaces(), indent=4)
    print('-'*60)
    print junos.get_interfaces()['me0']['mac_address']


