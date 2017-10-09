from napalm_base import get_network_driver
from pprint import pprint

junos_driver = get_network_driver('junos')
junos_device = junos_driver(hostname='172.30.179.107', username='pytraining', password='Poclab123', optional_args={'port': 830})

def change_configuration(device, configuration):
  device.load_merge_candidate(config=configuration)
  print(device.compare_config())
  device.commit_config()

print('-'*60)
junos_device.open()
change_configuration(junos_device,"system {host-name newhostname;}")
print('-'*60)

'''
# python configure.py
------------------------------------------------------------
[edit system]
-  host-name ex4200-7;
+  host-name newhostname;
------------------------------------------------------------
'''
