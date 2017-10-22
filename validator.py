import os
from yaml import load
from jinja2 import Template
from napalm_base import get_network_driver
from pprint import pprint

inventory_f=open('python_inventory.yml', 'r')
inventory_s=inventory_f.read()
inventory_f.close()
python_inventory=load(inventory_s)

f=open('validate.j2')
s=f.read()
f.close()
validate_template=Template(s)

# make sure the directory validatation exists
cwd = os.getcwd()
validation_directory = os.path.dirname(cwd + "/validation/")
if not os.path.exists(validation_directory):
    os.makedirs(validation_directory)

junos_driver = get_network_driver('junos')

for device_item in python_inventory:
    print '-'*60
    print ('rendering the template validate.j2 for device ' + device_item)
    f=open(python_inventory[device_item]['vars'])
    s=f.read()
    f.close()
    vars=load(s)
    validator_file=open(validation_directory + '/' + device_item + '.yml','w')
    validator_file.write(validate_template.render(vars))
    validator_file.close()
    print '-'*60
    print ('auditing the device ' + device_item)
    junos_device = junos_driver(hostname=python_inventory[device_item]['ip'], username='pytraining', password='Poclab123', optional_args={'port': 830})
    junos_device.open()
    pprint(junos_device.compliance_report(validation_directory + '/' + device_item + '.yml'))
    print '-'*60
    print ('the device ' + device_item + " complies:")
    print (junos_device.compliance_report(validation_directory + '/' + device_item + '.yml')['complies'])
    junos_device.close()

"""
# python validator.py
------------------------------------------------------------
rendering the template validate.j2 for device ex4200_8
------------------------------------------------------------
auditing the device ex4200_8
{u'complies': True,
 'get_bgp_neighbors_detail': {u'complies': True,
                              u'extra': [],
                              u'missing': [],
                              u'present': {'inet.0': {u'complies': True,
                                                      u'nested': True}}},
 u'skipped': []}
------------------------------------------------------------
the device ex4200_8 complies:
True
------------------------------------------------------------
rendering the template validate.j2 for device ex4200_7
------------------------------------------------------------
auditing the device ex4200_7
{u'complies': True,
 'get_bgp_neighbors_detail': {u'complies': True,
                              u'extra': [],
                              u'missing': [],
                              u'present': {'inet.0': {u'complies': True,
                                                      u'nested': True}}},
 u'skipped': []}
------------------------------------------------------------
the device ex4200_7 complies:
True
------------------------------------------------------------
rendering the template validate.j2 for device ex4200_12
------------------------------------------------------------
auditing the device ex4200_12
{u'complies': True,
 'get_bgp_neighbors_detail': {u'complies': True,
                              u'extra': [],
                              u'missing': [],
                              u'present': {'inet.0': {u'complies': True,
                                                      u'nested': True}}},
 u'skipped': []}
------------------------------------------------------------
the device ex4200_12 complies:
True

"""
"""
# ls validation
ex4200_12.yml  ex4200_7.yml  ex4200_8.yml
"""
"""
# more validation/ex4200_8.yml
- get_bgp_neighbors_detail:
    inet.0:

      209:
       - connection_state: Established

      204:
       - connection_state: Established
"""
"""
# more validation/ex4200_7.yml
- get_bgp_neighbors_detail:
    inet.0:

      210:
       - connection_state: Established

      204:
       - connection_state: Established

"""

