from napalm_base import get_network_driver
from yaml import load
from jinja2 import Template
import time
import os

# getting template
f=open('bgp.j2')
s=f.read()
f.close()
bgp_template=Template(s)

# getting inventory in a python data structure. 
inventory_f=open('python_inventory.yml', 'r')
inventory_s=inventory_f.read()
inventory_f.close()
python_inventory=load(inventory_s)
# python_inventory
# type (python_inventory)
# pprint (python_inventory)
# print python_inventory['ex4200-7']
# python_inventory['ex4200-7']
# python_inventory['ex4200-7']['ip']
# python_inventory['ex4200-7']['vars']
# type(python_inventory['ex4200-7']['vars'])
# for item in python_inventory:
#     print item
#     print python_inventory[item]
#     print python_inventory[item]['ip']
#     print python_inventory[item]['vars']
#     print '-'*60


# make sure the directory render exists
cwd = os.getcwd()
# cwd
render_directory = os.path.dirname(cwd + "/render/")
# render_directory
# os.path.exists(render_directory)
if not os.path.exists(render_directory):
    os.makedirs(render_directory)
# os.path.exists(render_directory)

def change_configuration(device, configuration):
       device.load_merge_candidate(filename=configuration)
       print(device.compare_config())
       device.commit_config()

for device_item in python_inventory:
    print '-'*60
    print ('rendering the template for device ' + device_item)
    f=open(python_inventory[device_item]['vars'])
    s=f.read()
    f.close()
    vars=load(s)
    bgp_conf=open(render_directory + '/' + device_item + '_bgp.txt','w')
    bgp_conf.write(bgp_template.render(vars))
    bgp_conf.close()
    print '-'*60
    print ('configuring the device ' + device_item)
    junos_driver = get_network_driver('junos')
    junos_device = junos_driver(hostname=python_inventory[device_item]['ip'], username='pytraining', password='Poclab123', optional_args={'port': 830})
    junos_device.open()
    change_configuration(junos_device, render_directory + '/' + device_item + '_bgp.txt')
    junos_device.close()

print '-'*60
print ('audit will start in 15 seconds')
time.sleep(15)

for device_item in python_inventory:
    print '-'*60
    print ('printing bgp sessions state for device '+ device_item)
    junos_device = junos_driver(hostname=python_inventory[device_item]['ip'], username='pytraining', password='Poclab123', optional_args={'port': 830})
    junos_device.open()
    for bgp_item in junos_device.get_bgp_neighbors_detail()['global']:
        print (junos_device.get_bgp_neighbors_detail()['global'][bgp_item][0]['remote_address'] + ' is ' + junos_device.get_bgp_neighbors_detail()['global'][bgp_item][0]['connection_state'])
    junos_device.close()

'''
# python ./configure_bgp_topology.py
------------------------------------------------------------
rendering the template for device ex4200_8
------------------------------------------------------------
configuring the device ex4200_8
[edit]
+  protocols {
+      bgp {
+          group underlay {
+              type external;
+              import bgp-in;
+              export bgp-out;
+              local-as 210;
+              multipath multiple-as;
+              neighbor 192.168.10.5 {
+                  peer-as 209;
+              }
+              neighbor 192.168.10.3 {
+                  peer-as 204;
+              }
+          }
+      }
+      lldp {
+          interface ge-0/0/0.0;
+          interface ge-0/0/1.0;
+      }
+  }
------------------------------------------------------------
rendering the template for device ex4200_7
------------------------------------------------------------
configuring the device ex4200_7
[edit protocols]
+   bgp {
+       group underlay {
+           type external;
+           import bgp-in;
+           export bgp-out;
+           local-as 209;
+           multipath multiple-as;
+           neighbor 192.168.10.4 {
+               peer-as 210;
+           }
+           neighbor 192.168.10.0 {
+               peer-as 204;
+           }
+       }
+   }
------------------------------------------------------------
rendering the template for device ex4200_12
------------------------------------------------------------
configuring the device ex4200_12
[edit interfaces]
+   ge-0/0/0 {
+       unit 0 {
+           description ex4200-7;
+           family inet {
+               address 192.168.10.0/31;
+           }
+       }
+   }
+   ge-0/0/1 {
+       unit 0 {
+           description ex4200-8;
+           family inet {
+               address 192.168.10.3/31;
+           }
+       }
+   }
[edit routing-options]
+   forwarding-table {
+       export bgp-ecmp;
+   }
[edit]
+  protocols {
+      bgp {
+          group underlay {
+              type external;
+              import bgp-in;
+              export bgp-out;
+              local-as 204;
+              multipath multiple-as;
+              neighbor 192.168.10.1 {
+                  peer-as 209;
+              }
+              neighbor 192.168.10.2 {
+                  peer-as 210;
+              }
+          }
+      }
+      lldp {
+          interface ge-0/0/0.0;
+          interface ge-0/0/1.0;
+      }
+  }
+  policy-options {
+      policy-statement bgp-ecmp {
+          then {
+              load-balance per-packet;
+          }
+      }
+      policy-statement bgp-in {
+          then accept;
+      }
+      policy-statement bgp-out {
+          then accept;
+      }
+  }
------------------------------------------------------------
audit will start in 15 seconds
------------------------------------------------------------
printing bgp sessions state for device ex4200_8
192.168.10.5 is Established
192.168.10.3 is Established
------------------------------------------------------------
printing bgp sessions state for device ex4200_7
192.168.10.4 is Established
192.168.10.0 is Established
------------------------------------------------------------
printing bgp sessions state for device ex4200_12
192.168.10.1 is Established
192.168.10.2 is Established

'''


