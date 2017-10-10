from napalm_base import get_network_driver
from pprint import pprint
from json import dumps

junos_driver = get_network_driver('junos')

junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

with junos_driver(**junos_device) as junos:
  print('-'*60)
  pprint(junos.get_bgp_neighbors_detail(neighbor_address='192.168.0.4'))
  print('-'*60)
  print dumps(junos.get_bgp_neighbors_detail(), indent=4)
  print('-'*60)
  for item in junos.get_bgp_neighbors_detail()['global']:
     print item
  print('-'*60)
  print junos.get_bgp_neighbors_detail()['global'][104][0]['connection_state']
  print junos.get_bgp_neighbors_detail()['global'][110][0]['connection_state']
  print('-'*60)
  for item in junos.get_bgp_neighbors_detail()['global']:
    print junos.get_bgp_neighbors_detail()['global'][item][0]['connection_state']


'''
# python junos_get_bgp_neighbors_details.py
------------------------------------------------------------
{u'global': {110: [{u'accepted_prefix_count': 5,
                    u'active_prefix_count': 2,
                    u'advertised_prefix_count': 6,
                    u'configured_holdtime': 90,
                    u'configured_keepalive': 30,
                    u'connection_state': u'Established',
                    u'export_policy': u'bgp-out',
                    u'flap_count': 1,
                    u'holdtime': 90,
                    u'import_policy': u'bgp-in',
                    u'input_messages': 166945,
                    u'input_updates': 10,
                    u'keepalive': 30,
                    u'last_event': u'RecvKeepAlive',
                    u'local_address': u'192.168.0.5',
                    u'local_address_configured': False,
                    u'local_as': 109,
                    u'local_as_prepend': True,
                    u'local_port': 53714,
                    u'messages_queued_out': 0,
                    u'multihop': False,
                    u'multipath': True,
                    u'output_messages': 166898,
                    u'output_updates': 3,
                    u'previous_connection_state': u'OpenConfirm',
                    u'received_prefix_count': 5,
                    u'remote_address': u'192.168.0.4',
                    u'remote_as': 110,
                    u'remote_port': 179,
                    u'remove_private_as': False,
                    u'router_id': u'192.179.0.73',
                    u'routing_table': u'global',
                    u'suppress_4byte_as': False,
                    u'suppressed_prefix_count': 0,
                    u'up': True}]}}
------------------------------------------------------------
{
    "global": {
        "104": [
            {
                "suppress_4byte_as": false,
                "local_as_prepend": true,
                "connection_state": "Established",
                "multihop": false,
                "input_messages": 261766,
                "previous_connection_state": "OpenConfirm",
                "output_messages": 166895,
                "remove_private_as": false,
                "multipath": true,
                "messages_queued_out": 0,
                "keepalive": 30,
                "remote_as": 104,
                "local_port": 54024,
                "active_prefix_count": 2,
                "configured_holdtime": 90,
                "routing_table": "global",
                "flap_count": 0,
                "suppressed_prefix_count": 0,
                "local_address": "192.168.0.1",
                "remote_port": 179,
                "input_updates": 94872,
                "configured_keepalive": 30,
                "router_id": "192.179.0.74",
                "export_policy": "bgp-out",
                "local_as": 109,
                "remote_address": "192.168.0.0",
                "advertised_prefix_count": 5,
                "local_address_configured": false,
                "import_policy": "bgp-in",
                "last_event": "RecvKeepAlive",
                "accepted_prefix_count": 5,
                "up": true,
                "output_updates": 2,
                "received_prefix_count": 5,
                "holdtime": 90
            }
        ],
        "110": [
            {
                "suppress_4byte_as": false,
                "local_as_prepend": true,
                "connection_state": "Established",
                "multihop": false,
                "input_messages": 166945,
                "previous_connection_state": "OpenConfirm",
                "output_messages": 166898,
                "remove_private_as": false,
                "multipath": true,
                "messages_queued_out": 0,
                "keepalive": 30,
                "remote_as": 110,
                "local_port": 53714,
                "active_prefix_count": 2,
                "configured_holdtime": 90,
                "routing_table": "global",
                "flap_count": 1,
                "suppressed_prefix_count": 0,
                "local_address": "192.168.0.5",
                "remote_port": 179,
                "input_updates": 10,
                "configured_keepalive": 30,
                "router_id": "192.179.0.73",
                "export_policy": "bgp-out",
                "local_as": 109,
                "remote_address": "192.168.0.4",
                "advertised_prefix_count": 6,
                "local_address_configured": false,
                "import_policy": "bgp-in",
                "last_event": "RecvKeepAlive",
                "accepted_prefix_count": 5,
                "up": true,
                "output_updates": 3,
                "received_prefix_count": 5,
                "holdtime": 90
            }
        ]
    }
}
------------------------------------------------------------
104
110
------------------------------------------------------------
Established
Established
------------------------------------------------------------
Established
Established

'''





