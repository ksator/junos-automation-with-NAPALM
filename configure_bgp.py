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

'''
# python ./configure_bgp.py
------------------------------------------------------------
rendering bgp template
------------------------------------------------------------
configuring device
[edit interfaces]
+   ge-0/0/0 {
+       unit 0 {
+           description ex4200-12;
+           family inet {
+               address 192.168.10.1/31;
+           }
+       }
+   }
+   ge-0/0/1 {
+       unit 0 {
+           description ex4200-8;
+           family inet {
+               address 192.168.10.5/31;
+           }
+       }
+   }
[edit routing-options]
+  router-id 192.179.0.107;
+  forwarding-table {
+      export bgp-ecmp;
+  }
[edit]
+  protocols {
+      bgp {
+          group underlay {
+              type external;
+              import bgp-in;
+              export bgp-out;
+              local-as 209;
+              multipath multiple-as;
+              neighbor 192.168.10.4 {
+                  peer-as 210;
+              }
+              neighbor 192.168.10.0 {
+                  peer-as 204;
+              }
+          }
+      }
+      lldp {
+          interface ge-0/0/1.0;
+          interface ge-0/0/0.0;
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
printing bgp sessions state
Established
Established

'''
