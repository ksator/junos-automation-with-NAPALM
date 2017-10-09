from napalm_base import get_network_driver

junos_driver = get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

with junos_driver(**junos_device) as junos:
  print junos.get_config()

