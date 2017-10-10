from napalm_base import get_network_driver
from yaml import load
from jinja2 import Template
import time

# getting template
f=open('bgp.j2')
s=f.read()
f.close()
bgp_template=Template(s)

# getting variables
f=open('ex4200_7_bgp.yml')
s=f.read()
f.close()
bgp_vars_ex4200_7=load(s)

# rendering the template
print('-'*60)
print 'rendering bgp template'
bgp_conf=open('bgp_ex4200_7.txt','w')
bgp_conf.write(bgp_template.render(bgp_vars_ex4200_7))
bgp_conf.close()

# configuring the device
print('-'*60)
print 'configuring device'
junos_driver = get_network_driver('junos')
junos_device = junos_driver(hostname='172.30.179.107', username='pytraining', password='Poclab123', optional_args={'port': 830})

def change_configuration(device, configuration):
  device.load_merge_candidate(filename=configuration)
  print(device.compare_config())
  device.commit_config()

junos_device.open()
change_configuration(junos_device,"bgp_ex4200_7.txt")

# auditing the device
print('-'*60)
print 'printing bgp sessions state'
time.sleep(20)
for item in junos_device.get_bgp_neighbors_detail()['global']:
    print junos_device.get_bgp_neighbors_detail()['global'][item][0]['connection_state']


