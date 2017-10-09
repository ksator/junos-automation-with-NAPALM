from napalm_base import get_network_driver
from pprint import pprint

junos_driver =  get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

with junos_driver(**junos_device) as junos:
    pprint(junos.get_facts())


'''
# python junos_get_facts.py
{u'fqdn': u'ex4300-9.poc-nl.jnpr.net',
 u'hostname': u'ex4300-9',
 u'interface_list': ['ge-0/0/0',
                     'pfe-0/0/0',
                     'pfh-0/0/0',
                     'ge-0/0/1',
                     'ge-0/0/2',
                     'ge-0/0/3',
                     'ge-0/0/4',
                     'ge-0/0/5',
                     'ge-0/0/6',
                     'ge-0/0/7',
                     'ge-0/0/8',
                     'ge-0/0/9',
                     'ge-0/0/10',
                     'ge-0/0/11',
                     'ge-0/0/12',
                     'ge-0/0/13',
                     'ge-0/0/14',
                     'ge-0/0/15',
                     'ge-0/0/16',
                     'ge-0/0/17',
                     'ge-0/0/18',
                     'ge-0/0/19',
                     'ge-0/0/20',
                     'ge-0/0/21',
                     'ge-0/0/22',
                     'ge-0/0/23',
                     '.local.',
                     'bme0',
                     'dsc',
                     'gre',
                     'ipip',
                     'irb',
                     'jsrv',
                     'lo0',
                     'lsi',
                     'me0',
                     'mtun',
                     'pimd',
                     'pime',
                     'tap',
                     'vme'],
 u'model': u'EX4300-24T',
 u'os_version': u'15.1R5.5',
 u'serial_number': u'PG3713290006',
 u'uptime': 4518360,
 u'vendor': u'Juniper'}
'''

