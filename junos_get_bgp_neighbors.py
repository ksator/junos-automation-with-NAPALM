from json import dumps
from napalm_base import get_network_driver

junos_driver = get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

with junos_driver(**junos_device) as junos:
  print('-'*60)
  print junos.get_bgp_neighbors()
  print('-'*60)
  print dumps(junos.get_bgp_neighbors(), indent=4)
  print('-'*60)
  print junos.get_bgp_neighbors()['global']['peers']['192.168.0.4']['uptime']


'''
# python junos_get_bgp_neighbors.py
------------------------------------------------------------
{u'global': {u'router_id': u'192.179.0.95', u'peers': {u'192.168.0.0': {u'is_enabled': True, u'uptime': 4525781, u'remote_as': 104, u'address_family': {u'ipv4': {u'sent_prefixes': 5, u'accepted_prefixes': 5, u'received_prefixes': 5}, u'ipv6': {u'sent_prefixes': -1, u'accepted_prefixes': -1, u'received_prefixes': -1}}, u'remote_id': u'192.179.0.74', u'local_as': 109, u'is_up': True, u'description': u''}, '192.168.0.4': {u'is_enabled': True, u'uptime': 4525784, u'remote_as': 110, u'address_family': {u'ipv4': {u'sent_prefixes': 6, u'accepted_prefixes': 5, u'received_prefixes': 5}, u'ipv6': {u'sent_prefixes': -1, u'accepted_prefixes': -1, u'received_prefixes': -1}}, u'remote_id': u'192.179.0.73', u'local_as': 109, u'is_up': True, u'description': u''}}}}
------------------------------------------------------------
{
    "global": {
        "router_id": "192.179.0.95",
        "peers": {
            "192.168.0.0": {
                "is_enabled": true,
                "uptime": 4525781,
                "remote_as": 104,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 5,
                        "accepted_prefixes": 5,
                        "received_prefixes": 5
                    },
                    "ipv6": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    }
                },
                "remote_id": "192.179.0.74",
                "local_as": 109,
                "is_up": true,
                "description": ""
            },
            "192.168.0.4": {
                "is_enabled": true,
                "uptime": 4525784,
                "remote_as": 110,
                "address_family": {
                    "ipv4": {
                        "sent_prefixes": 6,
                        "accepted_prefixes": 5,
                        "received_prefixes": 5
                    },
                    "ipv6": {
                        "sent_prefixes": -1,
                        "accepted_prefixes": -1,
                        "received_prefixes": -1
                    }
                },
                "remote_id": "192.179.0.73",
                "local_as": 109,
                "is_up": true,
                "description": ""
            }
        }
    }
}
------------------------------------------------------------
4525930

'''
