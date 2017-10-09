
## About NAPALM

NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library to interact with different network operating systems.  

You can use NAPALM with: 
- [Python](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/README.md#how-to-use-napalm-with-python)
- [CLI](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/README.md#how-to-use-napalm-with-cli)
- [Ansible](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/README.md#how-to-use-napalm-with-ansible)
- [StackStorm](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/README.md#how-to-use-the-napalm-pack-for-stackstorm)
- [SaltStack](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/README.md#how-to-use-napalm-with-saltstack)


NAPALM source code: https://github.com/napalm-automation/napalm  
NAPALM doc: https://napalm.readthedocs.io/en/latest/index.html  

## How to use NAPALM with Python

For help with Python programming, you can refer to https://github.com/ksator/python-training-for-network-engineers 

Installation:  
```
sudo pip install napalm
sudo pip install napalm-yang
```

Open a connection to the device
```
>>> import napalm
>>> from pprint import pprint as pp
>>> driver = napalm.get_network_driver('junos')
>>> device = driver(hostname='172.30.179.107', username='pytraining', password='Poclab123', optional_args={'port': 830})
>>> device.open()
>>> device.username
'pytraining'
>>> device.is_alive()
{u'is_alive': True}
>>>
```
Load a configuration to the device 
```
# more hostname_config.txt
system {
    host-name newhostname;
}
```
```
>>> device.load_merge_candidate(filename='hostname_config.txt')
>>> device.compare_config()
'[edit system]\n-  host-name ex4200-7;\n+  host-name newhostname;'
>>> print device.compare_config()
[edit system]
-  host-name ex4200-7;
+  host-name newhostname;
>>> device.rollback()
```
Use a getter:
```
>>> pp(device.get_facts())
{u'fqdn': u'newhostname.poc-nl.jnpr.net',
 u'hostname': u'newhostname',
 u'interface_list': ['ge-0/0/0',
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
                     'ge-0/0/24',
                     'ge-0/0/25',
                     'ge-0/0/26',
                     'ge-0/0/27',
                     'ge-0/0/28',
                     'ge-0/0/29',
                     'ge-0/0/30',
                     'ge-0/0/31',
                     'ge-0/0/32',
                     'ge-0/0/33',
                     'ge-0/0/34',
                     'ge-0/0/35',
                     'ge-0/0/36',
                     'ge-0/0/37',
                     'ge-0/0/38',
                     'ge-0/0/39',
                     'ge-0/0/40',
                     'ge-0/0/41',
                     'ge-0/0/42',
                     'ge-0/0/43',
                     'ge-0/0/44',
                     'ge-0/0/45',
                     'ge-0/0/46',
                     'ge-0/0/47',
                     '.local.',
                     'vcp-0',
                     'vcp-1',
                     'bme0',
                     'dsc',
                     'gre',
                     'ipip',
                     'lo0',
                     'lsi',
                     'me0',
                     'mtun',
                     'pimd',
                     'pime',
                     'tap',
                     'vlan',
                     'vme'],
 u'model': u'EX4200-48T',
 u'os_version': u'12.3R11.2',
 u'serial_number': u'BP0208111225',
 u'uptime': 4527600,
 u'vendor': u'Juniper'}
```
Close the connection to the device
```
>>> device.is_alive()
{u'is_alive': True}
>>> device.close()
>>> device.is_alive()
{u'is_alive': False}
>>> exit()
```

## NAPALM and OpenConfig
For help with OpenConfig you can refer to:  
- https://github.com/ksator/openconfig-demo-with-juniper-devices
- https://github.com/ksator/openconfig-demo-with-juniper-devices/wiki 

For help with NAPALM and OpenConfig, you can refer to: 
- https://github.com/napalm-automation/napalm-yang/blob/develop/interactive_demo/tutorial.ipynb
- https://www.dravetech.com/blog/2016/05/06/oc-napalm.html

Examples: 
- [Parse native configuration and return and OpenConfig object](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/native_to_openconfig.py)
- [Translate OpenConfig to native configuration](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/openconfig_to_native.py)

## How to use NAPALM with CLI


To get the help, run this command:  
```
cl_napalm_configure --help
```
Example with dry run:
```
ksator@ubuntu:~$ cl_napalm_configure --user pytraining --vendor junos --strategy merge --dry-run 172.30.177.170 napalm/conf.txt 
Enter password: 
[edit system]
-  host-name mx80-17;
+  host-name newhostname;
ksator@ubuntu:~$ 
```


## How to use NAPALM with Ansible 
For help with Ansible you can refer to https://github.com/ksator/ansible-training-for-junos-automation 

## How to use the NAPALM pack for StackStorm
- For help with StackStorm you can refer to https://github.com/ksator/junos-automation-with-stackstorm 
- For help regarding the NAPALM pack for StackStorm you can refer to https://github.com/ksator/junos-automation-with-stackstorm/wiki/06.-napalm-pack

## How to use NAPALM with SaltStack
- For help with SaltStack you can refer to https://github.com/ksator/junos-automation-with-saltstack
- For help with SaltStack and NAPALM you can refer to https://www.nanog.org/sites/default/files/NANOG68%20Network%20Automation%20with%20Salt%20and%20NAPALM%20Mircea%20Ulinic%20Cloudflare%20(1).pdf 



