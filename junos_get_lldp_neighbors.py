from napalm_base import get_network_driver
from json import dumps
from pprint import pprint

junos_driver = get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

print('-'*60)
with junos_driver(**junos_device) as junos:
     pprint(junos.get_lldp_neighbors())
'''
{'ge-0/0/0': [{'hostname': u'ex4300-17', 'port': u'ge-0/0/0'}],
 'ge-0/0/1': [{'hostname': u'ex4300-18', 'port': u'ge-0/0/0'}]}
'''
print('-'*60)
with junos_driver(**junos_device) as junos:
     print(junos.get_lldp_neighbors())
'''
{'ge-0/0/1': [{'hostname': u'ex4300-18', 'port': u'ge-0/0/0'}], 'ge-0/0/0': [{'hostname': u'ex4300-17', 'port': u'ge-0/0/0'}]}
'''
print('-'*60)
with junos_driver(**junos_device) as junos:
     print dumps(junos.get_lldp_neighbors(), indent=4)
'''
{
    "ge-0/0/1": [
        {
            "hostname": "ex4300-18",
            "port": "ge-0/0/0"
        }
    ],
    "ge-0/0/0": [
        {
            "hostname": "ex4300-17",
            "port": "ge-0/0/0"
        }
    ]
}
'''
print('-'*60)
with junos_driver(**junos_device) as junos:
   if junos.get_lldp_neighbors()['ge-0/0/1'][0]['hostname']!="ex4300-18":
       print "wrong cabling on ge-0/0/1 ..."

