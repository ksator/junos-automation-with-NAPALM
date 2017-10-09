from napalm_base import get_network_driver
from pprint import pprint

junos_driver = get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

print('-'*60)

with junos_driver(**junos_device) as junos:
  pprint(junos.get_bgp_config())
  print('-'*60)
  print junos.get_bgp_config()['underlay']['neighbors']['192.168.0.4']['remote_as']

'''
------------------------------------------------------------
{'underlay': {u'apply_groups': [],
              u'description': u'',
              u'export_policy': u'bgp-out',
              u'import_policy': u'bgp-in',
              u'local_address': u'',
              u'local_as': 109,
              u'multihop_ttl': 0,
              u'multipath': True,
              u'neighbors': {u'192.168.0.0': {u'authentication_key': u'',
                                              u'description': u'',
                                              u'export_policy': u'',
                                              u'import_policy': u'',
                                              u'local_address': u'',
                                              u'local_as': 0,
                                              u'nhs': False,
                                              u'prefix_limit': {},
                                              u'remote_as': 104,
                                              u'route_reflector_client': False},
                             u'192.168.0.4': {u'authentication_key': u'',
                                              u'description': u'',
                                              u'export_policy': u'',
                                              u'import_policy': u'',
                                              u'local_address': u'',
                                              u'local_as': 0,
                                              u'nhs': False,
                                              u'prefix_limit': {},
                                              u'remote_as': 110,
                                              u'route_reflector_client': False}},
              u'prefix_limit': {},
              u'remote_as': 0,
              u'remove_private_as': False,
              u'type': u'external'}}
------------------------------------------------------------
104
'''
