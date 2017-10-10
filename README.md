
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

### Installation:  
```
sudo pip install napalm
sudo pip install napalm-yang
```

### Open a connection to the device
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
### Load a configuration to the device 
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
### Use a getter:
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
### Close the connection to the device
```
>>> device.is_alive()
{u'is_alive': True}
>>> device.close()
>>> device.is_alive()
{u'is_alive': False}
>>> exit()
```

### More examples
For more examples, you can look at the python scripts at the [root of the repository](https://github.com/ksator/junos-automation-with-NAPALM). 

## NAPALM and OpenConfig

### Help: 
- For help with OpenConfig you can refer to:  
    - https://github.com/ksator/openconfig-demo-with-juniper-devices
    - https://github.com/ksator/openconfig-demo-with-juniper-devices/wiki 
- For help with NAPALM and OpenConfig, you can refer to: 
    - https://github.com/napalm-automation/napalm-yang/blob/develop/interactive_demo/tutorial.ipynb
    - https://www.dravetech.com/blog/2016/05/06/oc-napalm.html

### Examples: 
- [Parse native configuration and return and OpenConfig object](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/native_to_openconfig.py)
- [Translate OpenConfig to native configuration](https://github.com/ksator/junos-automation-with-NAPALM/blob/master/openconfig_to_native.py)

## How to use NAPALM with CLI


### Help  
To get the help, run this command:  
```
napalm --help
```
### Getters  
```
# napalm --user pytraining --password Poclab123 --vendor junos 172.30.177.170 call get_facts
{
    "os_version": "17.2R1.13",
    "uptime": 1883340,
    "interface_list": [
        "lc-0/0/0",
        "pfe-0/0/0",
        "pfh-0/0/0",
        "xe-0/0/0",
        "xe-0/0/1",
        "xe-0/0/2",
        "xe-0/0/3",
        "ge-1/0/0",
        "ge-1/0/1",
        "ge-1/0/2",
        "ge-1/0/3",
        "ge-1/0/4",
        "ge-1/0/5",
        "ge-1/0/6",
        "ge-1/0/7",
        "ge-1/0/8",
        "ge-1/0/9",
        "ge-1/0/10",
        "ge-1/0/11",
        "ge-1/1/0",
        "ge-1/1/1",
        "ge-1/1/2",
        "ge-1/1/3",
        "ge-1/1/4",
        "ge-1/1/5",
        "ge-1/1/6",
        "ge-1/1/7",
        "ge-1/1/8",
        "ge-1/1/9",
        "ge-1/1/10",
        "ge-1/1/11",
        "ge-1/2/0",
        "ge-1/2/1",
        "ge-1/2/2",
        "ge-1/2/3",
        "ge-1/2/4",
        "ge-1/2/5",
        "ge-1/2/6",
        "ge-1/2/7",
        "ge-1/2/8",
        "ge-1/2/9",
        "ge-1/2/10",
        "ge-1/2/11",
        "ge-1/3/0",
        "ge-1/3/1",
        "ge-1/3/2",
        "ge-1/3/3",
        "ge-1/3/4",
        "ge-1/3/5",
        "ge-1/3/6",
        "ge-1/3/7",
        "ge-1/3/8",
        "ge-1/3/9",
        "ge-1/3/10",
        "ge-1/3/11",
        ".local.",
        "cbp0",
        "demux0",
        "dsc",
        "em0",
        "em1",
        "esi",
        "fxp0",
        "gre",
        "ipip",
        "irb",
        "jsrv",
        "lo0",
        "lsi",
        "me0",
        "mtun",
        "pimd",
        "pime",
        "pip0",
        "pp0",
        "rbeb",
        "tap",
        "vtep"
    ],
    "vendor": "Juniper",
    "serial_number": "E3061",
    "model": "MX80-48T",
    "hostname": "mx80-17",
    "fqdn": "mx80-17.poc-nl.jnpr.net"
}
```
```
# napalm --user pytraining --password Poclab123 --vendor junos 172.30.177.170 call get_bgp_config
{
    "IBGP": {
        "neighbors": {
            "192.181.0.28": {
                "export_policy": "",
                "remote_as": 100,
                "route_reflector_client": false,
                "prefix_limit": {},
                "local_as": 0,
                "nhs": false,
                "import_policy": "",
                "local_address": "",
                "authentication_key": "",
                "description": ""
            },
            "192.181.0.25": {
                "export_policy": "",
                "remote_as": 0,
                "route_reflector_client": false,
                "prefix_limit": {},
                "local_as": 0,
                "nhs": false,
                "import_policy": "",
                "local_address": "",
                "authentication_key": "",
                "description": ""
            },
            "192.177.0.147": {
                "export_policy": "",
                "remote_as": 100,
                "route_reflector_client": false,
                "prefix_limit": {},
                "local_as": 0,
                "nhs": false,
                "import_policy": "",
                "local_address": "",
                "authentication_key": "",
                "description": ""
            },
            "192.181.0.27": {
                "export_policy": "",
                "remote_as": 100,
                "route_reflector_client": false,
                "prefix_limit": {},
                "local_as": 0,
                "nhs": false,
                "import_policy": "",
                "local_address": "",
                "authentication_key": "",
                "description": ""
            }
        },
        "export_policy": "",
        "remote_as": 0,
        "description": "",
        "prefix_limit": {},
        "local_as": 0,
        "multihop_ttl": 0,
        "apply_groups": [],
        "local_address": "192.177.0.170",
        "remove_private_as": false,
        "multipath": false,
        "type": "internal",
        "import_policy": ""
    }
}

```
```
# napalm --user pytraining --password Poclab123 --vendor junos 172.30.177.170 call get_bgp_neighbors
{
    "global": {
        "router_id": "",
        "peers": {
            "192.181.0.28": {
                "is_enabled": true,
                "uptime": 1120757,
                "remote_as": 100,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    },
                    "ipv6": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    }
                },
                "remote_id": "",
                "local_as": 100,
                "is_up": false,
                "description": ""
            },
            "192.181.0.25": {
                "is_enabled": true,
                "uptime": 1120769,
                "remote_as": 100,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    },
                    "ipv6": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    }
                },
                "remote_id": "",
                "local_as": 100,
                "is_up": false,
                "description": ""
            },
            "192.177.0.147": {
                "is_enabled": true,
                "uptime": 1120770,
                "remote_as": 100,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    },
                    "ipv6": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    }
                },
                "remote_id": "",
                "local_as": 100,
                "is_up": false,
                "description": ""
            },
            "192.181.0.27": {
                "is_enabled": true,
                "uptime": 1120772,
                "remote_as": 100,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    },
                    "ipv6": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    }
                },
                "remote_id": "",
                "local_as": 100,
                "is_up": false,
                "description": ""
            }
        }
    }
}

```
### Commands  
```
# napalm --user pytraining --password Poclab123 --vendor junos 172.30.177.170 call cli --method-kwargs "commands=['show  version']"
{
    "show  version": "\nHostname: mx80-17\nModel: mx80-48t\nJunos: 17.2R1.13\nJUNOS Base OS boot [17.2R1.13]\nJUNOS Base OS Software Suite [17.2R1.13]\nJUNOS Crypto Software Suite [17.2R1.13]\nJUNOS Packet Forwarding Engine Support (MX80) [17.2R1.13]\nJUNOS Web Management [17.2R1.13]\nJUNOS Online Documentation [17.2R1.13]\nJUNOS SDN Software Suite [17.2R1.13]\nJUNOS Services Application Level Gateways [17.2R1.13]\nJUNOS Services Jflow Container package [17.2R1.13]\nJUNOS Services Stateful Firewall [17.2R1.13]\nJUNOS Services NAT [17.2R1.13]\nJUNOS Services RPM [17.2R1.13]\nJUNOS Services Captive Portal and Content Delivery Container package [17.2R1.13]\nJUNOS Macsec Software Suite [17.2R1.13]\nJUNOS Services Crypto [17.2R1.13]\nJUNOS Services IPSec [17.2R1.13]\nJUNOS DP Crypto Software Software Suite [17.2R1.13]\nJUNOS py-base-powerpc [17.2R1.13]\nJUNOS py-extensions-powerpc [17.2R1.13]\nJUNOS jsd [powerpc-17.2R1.13-jet-1]\nJUNOS Kernel Software Suite [17.2R1.13]\nJUNOS Routing Software Suite [17.2R1.13]\n"
}

```
### Configuration  

Example with dry run:
```
# napalm --user pytraining --password Poclab123 --vendor junos 172.30.177.170 configure hostname_config.txt --strategy merge --dry-run
[edit system]
-  host-name mx80-17;
+  host-name newhostname;
```
### Debug

## How to use NAPALM with Ansible 
For help with Ansible you can refer to https://github.com/ksator/ansible-training-for-junos-automation 

## How to use the NAPALM pack for StackStorm
- For help with StackStorm you can refer to https://github.com/ksator/junos-automation-with-stackstorm 
- For help regarding the NAPALM pack for StackStorm you can refer to https://github.com/ksator/junos-automation-with-stackstorm/wiki/06.-napalm-pack

## How to use NAPALM with SaltStack
- For help with SaltStack you can refer to https://github.com/ksator/junos-automation-with-saltstack
- For help with SaltStack and NAPALM you can refer to https://www.nanog.org/sites/default/files/NANOG68%20Network%20Automation%20with%20Salt%20and%20NAPALM%20Mircea%20Ulinic%20Cloudflare%20(1).pdf 



