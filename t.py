#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

import pprint

from cliparser import *


def test_cliparser_show_ip_route():

    '''
    Test the 'show ip ospf neighbor'
    '''
    print("\nDoing show ip route testing!!")

    # test two basic parsing
    data_1 = \
'''
Codes: C - connected, S - static, K - kernel,
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B I - iBGP, B E - eBGP,
       R - RIP, I - ISIS, A B - BGP Aggregate, A O - OSPF Summary,
       NG - Nexthop Group Static Route

Gateway of last resort:
 B I    0.0.0.0/0 [200/0] via 10.30.94.29, Vlan216

 B I    1.1.1.1/32 [200/0] via 10.30.94.6, Ethernet33
                           via 10.30.94.2, Vlan902
 B I    1.1.1.2/32 [200/0] via 10.30.94.6, Ethernet33
                           via 10.30.94.2, Vlan902
 O E2   1.1.2.1/32 [110/20] via 10.30.94.29, Vlan216
 O E1   10.4.92.28/32 [110/10120] via 10.30.94.6, Ethernet33
                                  via 10.30.94.2, Vlan902
 S      10.5.4.9/32 is directly connected, Null0
 O      10.5.251.0/24 [110/1523] via 10.30.94.29, Vlan216
 S      10.10.3.0/24 [1/0] via 10.70.15.73, Ethernet37
 S      10.12.1.0/24 [1/0] via 10.70.15.73, Ethernet37
 S      10.12.2.0/24 [1/0] via 10.70.15.73, Ethernet37
 O E1   10.13.5.101/32 [110/10120] via 10.30.94.6, Ethernet33
                                   via 10.30.94.2, Vlan902
 O E1   10.13.72.130/32 [110/10120] via 10.30.94.6, Ethernet33
                                    via 10.30.94.2, Vlan902
 S      10.13.0.0/17 [1/0] via 10.70.15.73, Ethernet37
 B I    10.14.0.0/16 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.0.0/20 [200/0] via 10.30.94.29, Vlan216
 O      10.15.30.12/30 [110/2230] via 10.30.94.29, Vlan216
 B I    10.15.32.0/20 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.48.0/20 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.64.0/20 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.80.0/20 [200/0] via 10.30.94.29, Vlan216
 O      10.15.110.16/30 [110/2230] via 10.30.94.29, Vlan216
 O      192.168.212.128/27 [110/1020] via 10.30.94.29, Vlan216
 O      192.168.212.160/27 [110/1120] via 10.30.94.29, Vlan216
 C      192.168.212.192/27 is directly connected, Vlan594
 C      192.168.212.224/27 is directly connected, Vlan596
'''
    attributes_1 = {'Command': 'show ip route', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip route:')
    assert len(result_1) > 1

    data_2 = \
'''
Codes: C - connected, S - static, K - kernel,
       O - OSPF, IA - OSPF inter area, E1 - OSPF external type 1,
       E2 - OSPF external type 2, N1 - OSPF NSSA external type 1,
       N2 - OSPF NSSA external type2, B I - iBGP, B E - eBGP,
       R - RIP, I - ISIS, A B - BGP Aggregate, A O - OSPF Summary,
       NG - Nexthop Group Static Route

Gateway of last resort:
 B I    0.0.0.0/0 [200/0] via 10.30.94.28, Vlan216

 B I    1.1.1.1/32 [200/0] via 10.30.94.2, Ethernet33
                           via 10.30.94.6, Vlan902
 B I    1.1.1.2/32 [200/0] via 10.30.94.6, Ethernet33
                           via 10.30.94.2, Vlan902
 O E2   9.1.2.1/32 [110/20] via 10.30.94.29, Vlan216
 O E1   10.4.92.28/32 [110/10120] via 10.30.94.6, Ethernet33
                                  via 10.30.94.2, Vlan902
 S      10.5.4.9/32 is directly connected, Null0
 O      10.5.251.0/24 [110/1523] via 10.30.94.29, Vlan216
 S      10.10.3.0/24 [1/0] via 10.70.15.73, Ethernet37
 S      10.12.1.0/24 [1/0] via 10.70.15.73, Ethernet37
 S      10.12.2.0/24 [1/0] via 10.70.15.73, Ethernet37
 O E1   10.13.5.101/32 [110/10120] via 10.30.94.6, Ethernet33
                                   via 10.30.94.2, Vlan902
 O E1   10.13.72.130/32 [110/10120] via 10.30.94.6, Ethernet33
                                    via 10.30.94.2, Vlan902
 S      10.13.0.0/17 [1/0] via 10.70.15.73, Ethernet37
 B I    10.14.0.0/16 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.0.0/20 [200/0] via 10.30.94.29, Vlan216
 O      10.15.30.12/30 [110/2230] via 10.30.94.29, Vlan216
 B I    10.15.32.0/20 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.48.0/20 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.64.0/20 [200/0] via 10.30.94.29, Vlan216
 B I    10.15.80.0/20 [200/0] via 10.30.94.29, Vlan216
 O      10.15.110.16/30 [110/2230] via 10.30.94.29, Vlan216
 O      192.168.212.128/27 [110/1020] via 10.30.94.29, Vlan216
 O      192.168.212.160/27 [110/1120] via 10.30.94.29, Vlan216
 C      192.168.212.192/27 is directly connected, Vlan594
 C      192.168.212.224/27 is directly connected, Vlan596
'''
    attributes_2 = {'Command': 'show ip route', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip route')
    assert len(result_2) > 1

    # make comparision of two route table with index of Interface
    # only find out the bgp state difference
    print('\nIP Route Table Comparisoin: index on network and mask compare next hop address')
    diff_config = {'index': ['NETWORK', 'MASK'],
                   'check': ['NEXT_HOP'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config, check_type='content')
    DiffTable.print_diff_entries(diff, print_same=True)

def test_cliparser_show_ip_bgp_sum():
    '''
    Test the 'show ip bgp summary' command
    '''
    print("\nDoing show ip bgp sum test!!")

    # test two basic parsing
    data_1 = \
'''BGP summary information for VRF default
Router identifier 10.30.95.2, local AS number 65200
Neighbor         V  AS      MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
10.30.31.3       4  65200   8091068   7454502    0    0  170d15h Estab  48     48
10.30.47.1       4  65200   7467159   7454575    0    0  862d16h Estab  46     46
10.30.94.34      4  65202   4765404   3668243    0    0   13d16h Estab  5      5
'''
    attributes_1 = {'Command': 'show ip bgp summary', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip bgp sum (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''BGP summary information for VRF default
Router identifier 10.30.95.2, local AS number 65200
Neighbor         V  AS      MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
10.30.31.3       4  65200   8091068   7454502    0    0  170d15h Estab  48     48
10.30.47.2       4  65200   7467159   7454575    0    0  862d16h Estab  46     46
10.30.94.34      4  65202   4765404   3668243    0    0   13d16h Estab  5      6
'''
    attributes_2 = {'Command': 'show ip bgp summary', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip bgp sum (data_2)')
    assert len(result_2) > 1

    # make comparision of two BGP table with index of BGP neighbor and AS number
    # only find out the bgp state difference
    print('\nBGP Table Comparision: index on BGP neighbor and AS number compare for BGP state only')
    diff_config = {'index' :['BGP_NEIGH', 'NEIGH_AS'],
                   'check' :['STATE'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] == []

    # make comparision of two BGP table with index of BGP neighbor and AS number
    # find out difference in recieved and published route
    print('\nBGP Table Comparision: index on BGP neighbor and AS number compare Rx and Tx prefix')
    diff_config = {'index' :['BGP_NEIGH', 'NEIGH_AS'],
                   'check' :['STATE_PFXRCD', 'STATE_PFXACC'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []

    # test direct parser with supplied template file and
    # should have same parse result as first one
    result_3 = CliParser.direct_parse_cli(data_1,
                                          './template/arista_eos_show_ip_bgp_summary.template')
    DiffTable.pretty_table_print(result_3, title='show ip bgp sum (direct call the template)')
    assert result_1 == result_3

    # test different version
    attributes_4 = {'Command': 'show ip bgp summary', 'Vendor': 'Arista', 'Version': 'V1'}
    parser = CliParser(attributes=attributes_4)
    result_4 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_4, title='show ip bgp sum (pick different version number)')
    assert len(result_4) > 1

def test_cliparser_show_ip_ospf_neighbor():
    '''
    Test the 'show ip ospf neighbor' command
    '''
    print("\nDoing show ip ospf neighbor!!")

    # test two basic parsing
    data_1 = \
'''
Neighbor ID     VRF    Pri   State            Dead Time   Address         Interface
10.30.47.1      default    0   FULL             00:00:03    10.30.94.6      Ethernet33
10.30.95.3      default    0   FULL             00:00:03    10.30.94.29     Vlan216
10.30.95.2      default    0   FULL             00:00:03    10.30.94.2      Vlan902
'''
    attributes_1 = {'Command': 'show ip ospf neighbor', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip ospf neighbor (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''
Neighbor ID     VRF    Pri   State            Dead Time   Address         Interface
10.30.47.1      default    0   FULL             00:00:03    10.30.94.6      Ethernet33
10.30.95.3      default    0   ACTI             00:00:03    10.30.94.29     Vlan216
10.30.95.4      default    0   FULL             00:00:03    10.30.94.2      Vlan902
'''
    attributes_2 = {'Command': 'show ip ospf neighbor', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip ospf neighbor (data_2)')
    assert len(result_2) > 1

    # make comparision of two ip ospf neighbor table with index of neighbor ID
    # only find out the ospf state difference
    print('\nOSPF Neighbor Table Comparision: index on neighbor ID and compare only state')
    diff_config = {'index' :['NEIGHBOR_ID'],
                   'check' :['STATE'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []

def test_cliparser_show_interfaces():
    '''
    Test the 'show interfaces' command
    '''
    print("\nDoing show interfaces!!")

    # test two basic parsing
    data_1 = \
'''
Ethernet1 is up, line protocol is up (connected)
  Hardware is Ethernet, address is 001c.73c6.5ed8 (bia 001c.73c6.5ed8)
  Description: jpnquipb2-sfc0
  Ethernet MTU 9214 bytes , BW 10000000 kbit
  Full-duplex, 10Gb/s, auto negotiation: off, uni-link: unknown
  Up 31 days, 5 hours, 52 minutes
  3 link status changes since last clear
  Last clearing of "show interface" counters never
  5 seconds input rate 5.54 Mbps (0.1% with framing overhead), 4973 packets/sec
  5 seconds output rate 9.87 Mbps (0.1% with framing overhead), 8008 packets/sec
     5805845678 packets input, 816641696401 bytes
     Received 9 broadcasts, 927867 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 471 input discards
     0 PAUSE input
     12784130051 packets output, 1712383713585 bytes
     Sent 3809604 broadcasts, 9930997253 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Ethernet2 is up, line protocol is up (connected)
  Hardware is Ethernet, address is 001c.73c6.5ed9 (bia 001c.73c6.5ed9)
  Description: jpntrademon1-sfc0
  Ethernet MTU 9214 bytes , BW 10000000 kbit
  Full-duplex, 10Gb/s, auto negotiation: off, uni-link: unknown
  Up 31 days, 5 hours, 51 minutes, 59 seconds
  3 link status changes since last clear
  Last clearing of "show interface" counters never
  5 seconds input rate 178 kbps (0.0% with framing overhead), 233 packets/sec
  5 seconds output rate 10.9 Mbps (0.1% with framing overhead), 9016 packets/sec
     403153367 packets input, 43460197482 bytes
     Received 56412 broadcasts, 25812941 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 0 input discards
     0 PAUSE input
     11637313925 packets output, 1712846239708 bytes
     Sent 3753193 broadcasts, 11436485635 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Vlan101 is up, line protocol is up (connected)
  Hardware is Vlan, address is 001c.73c6.5ed7 (bia 001c.73c6.5ed7)
  Description: vl101-1g
  Internet address is 10.30.81.3/24
  Secondary address is 10.30.92.3/24
  Broadcast address is 255.255.255.255
  Address determined by manual configuration
  IP MTU 1500 bytes
  Up 31 days, 5 hours, 41 minutes, 55 seconds
Vlan110 is up, line protocol is up (connected)
  Hardware is Vlan, address is 001c.73c6.5ed7 (bia 001c.73c6.5ed7)
  Description: vl110-10g
  Internet address is 10.30.80.3/24
  Broadcast address is 255.255.255.255
  Address determined by manual configuration
  IP MTU 1500 bytes
  Up 31 days, 5 hours, 52 minutes
'''
    attributes_1 = {'Command': 'show interfaces', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show interfaces (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''
Ethernet1 is down, line protocol is up (connected)
  Hardware is Ethernet, address is 001c.73c6.5ed8 (bia 001c.73c6.5ed8)
  Description: jpnquipb2-sfc0
  Ethernet MTU 9214 bytes , BW 10000000 kbit
  Full-duplex, 10Gb/s, auto negotiation: off, uni-link: unknown
  Up 31 days, 5 hours, 52 minutes
  3 link status changes since last clear
  Last clearing of "show interface" counters never
  5 seconds input rate 5.54 Mbps (0.1% with framing overhead), 4973 packets/sec
  5 seconds output rate 9.87 Mbps (0.1% with framing overhead), 8008 packets/sec
     5805845678 packets input, 816641696401 bytes
     Received 9 broadcasts, 927867 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 471 input discards
     0 PAUSE input
     12784130051 packets output, 1712383713585 bytes
     Sent 3809604 broadcasts, 9930997253 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Ethernet4 is up, line protocol is up (connected)
  Hardware is Ethernet, address is 001c.73c6.5ed9 (bia 001c.73c6.5ed9)
  Description: jpntrademon1-sfc0
  Ethernet MTU 9214 bytes , BW 10000000 kbit
  Full-duplex, 10Gb/s, auto negotiation: off, uni-link: unknown
  Up 31 days, 5 hours, 51 minutes, 59 seconds
  3 link status changes since last clear
  Last clearing of "show interface" counters never
  5 seconds input rate 178 kbps (0.0% with framing overhead), 233 packets/sec
  5 seconds output rate 10.9 Mbps (0.1% with framing overhead), 9016 packets/sec
     403153367 packets input, 43460197482 bytes
     Received 56412 broadcasts, 25812941 multicast
     0 runts, 0 giants
     0 input errors, 0 CRC, 0 alignment, 0 symbol, 0 input discards
     0 PAUSE input
     11637313925 packets output, 1712846239708 bytes
     Sent 3753193 broadcasts, 11436485635 multicast
     0 output errors, 0 collisions
     0 late collision, 0 deferred, 0 output discards
     0 PAUSE output
Vlan105 is up, line protocol is up (connected)
  Hardware is Vlan, address is 001c.73c6.5ed7 (bia 001c.73c6.5ed7)
  Description: vl101-1g
  Internet address is 10.30.81.3/24
  Secondary address is 10.30.92.3/24
  Broadcast address is 255.255.255.255
  Address determined by manual configuration
  IP MTU 1500 bytes
  Up 31 days, 5 hours, 41 minutes, 55 seconds
Vlan110 is up, line protocol is up (connected)
  Hardware is Vlan, address is 001c.73c6.5ed7 (bia 001c.73c6.5ed7)
  Description: vl110-10g
  Internet address is 10.30.80.3/24
  Broadcast address is 255.255.255.255
  Address determined by manual configuration
  IP MTU 1500 bytes
  Up 31 days, 5 hours, 52 minutes
'''
    attributes_2 = {'Command': 'show interfaces', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show interfaces (data_2)')
    assert len(result_2) > 1

    # make comparision of two ip ospf neighbor table with index of neighbor ID
    # only find out the ospf state difference
    print('\nInterface Table Comparsion: ')
    diff_config = {'index' :['INTERFACE'],
                   'check' :['LINK_STATUS'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []

def test_cliparser_show_ip_bgp():
    '''
    Test the 'show ip bgp' command
    '''
    print("\nDoing show ip bgp test!!")

    # test two basic parsing
    data_1 = \
'''
BGP routing table information for VRF default
Router identifier 10.30.95.1, local AS number 65200
Route status codes: s - suppressed, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

      Network             Next Hop         Metric  LocPref Weight Path
 * >  0.0.0.0/0           10.30.78.18      0       1000    0      65004 65003 65522 65521 65520 40827 174 i Or-ID: 10.30.79.1 C-LST: 10.30.31.3
 *    0.0.0.0/0           10.30.78.18      0       1000    0      65004 65003 65522 65521 65520 40827 174 i Or-ID: 10.30.79.1 C-LST: 10.30.47.254
 * >  1.1.1.1/32          10.30.47.5       0       100     0      i Or-ID: 165.39.11.126 C-LST: 10.30.31.3
 *    1.1.1.1/32          10.30.47.5       0       100     0      i Or-ID: 165.39.11.126 C-LST: 10.30.47.254
 * >  1.1.1.2/32          10.30.46.30      0       500     0      65512 i Or-ID: 165.39.11.126 C-LST: 10.30.31.3
 *    1.1.1.2/32          10.30.46.30      0       500     0      65512 i Or-ID: 165.39.11.126 C-LST: 10.30.47.254
 *    1.1.2.1/32          10.30.31.5       0       100     0      i Or-ID: 10.30.31.5 C-LST: 10.30.31.3
 * >  10.0.0.0/8          10.30.78.18      0       1000    0      65004 65003 ? Or-ID: 10.30.79.1 C-LST: 10.30.31.3
 *    10.0.0.0/8          10.30.78.18      0       1000    0      65004 65003 ? Or-ID: 10.30.79.1 C-LST: 10.30.47.254
 * >  10.14.0.0/16        10.15.110.17     0       1000    0      65118 65100 ? Or-ID: 10.30.63.2 C-LST: 10.30.31.3
 *    10.14.0.0/16        10.15.110.17     0       1000    0      65118 65100 ? Or-ID: 10.30.63.2 C-LST: 10.30.47.254
 * >  10.15.0.0/20        10.15.110.17     0       1000    0      65118 65110 ? Or-ID: 10.30.63.2 C-LST: 10.30.31.3
 *    10.15.0.0/20        10.15.110.17     0       1000    0      65118 65110 ? Or-ID: 10.30.63.2 C-LST: 10.30.47.254
'''
    attributes_1 = {'Command': 'show ip bgp vrf all', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip bgp (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''
BGP routing table information for VRF default
Router identifier 10.30.95.1, local AS number 65200
Route status codes: s - suppressed, * - valid, > - active, E - ECMP head, e - ECMP
                    S - Stale
Origin codes: i - IGP, e - EGP, ? - incomplete
AS Path Attributes: Or-ID - Originator ID, C-LST - Cluster List, LL Nexthop - Link Local Nexthop

      Network             Next Hop         Metric  LocPref Weight Path
 * >  0.0.0.0/0           10.30.78.19      0       1000    0      65004 65003 65522 65521 65520 40827 174 i Or-ID: 10.30.79.1 C-LST: 10.30.31.3
 *    0.0.0.0/0           10.30.78.18      0       1000    0      65004 65003 65522 65521 65520 40827 174 i Or-ID: 10.30.79.1 C-LST: 10.30.47.254
 * >  1.1.1.1/32          10.30.47.5       0       100     0      i Or-ID: 165.39.11.126 C-LST: 10.30.31.3
 *    1.1.1.1/32          10.30.47.5       0       100     0      i Or-ID: 165.39.11.126 C-LST: 10.30.47.254
 * >  1.1.1.2/32          10.30.46.30      0       500     0      65512 i Or-ID: 165.39.11.126 C-LST: 10.30.31.3
 *    1.1.1.2/32          10.30.46.30      0       500     0      65512 i Or-ID: 165.39.11.126 C-LST: 10.30.47.254
 *    1.1.2.1/32          10.30.31.5       0       100     0      i Or-ID: 10.30.31.5 C-LST: 10.30.31.3
 * >  10.0.0.0/8          10.30.78.18      0       1000    0      65004 65003 ? Or-ID: 10.30.79.1 C-LST: 10.30.31.3
 *    10.0.0.0/8          10.30.78.18      0       1000    0      65004 65003 ? Or-ID: 10.30.79.1 C-LST: 10.30.47.254
 * >  10.15.0.0/20        10.15.110.17     0       1000    0      65118 65110 ? Or-ID: 10.30.63.2 C-LST: 10.30.31.3
 *    10.15.0.0/20        10.15.110.17     0       1000    0      65118 65110 ? Or-ID: 10.30.63.2 C-LST: 10.30.47.254
 * >  10.15.32.0/20       10.15.110.17     0       1000    0      65118 65110 65114 65112 ? Or-ID: 10.30.63.2 C-LST: 10.30.31.3
'''
    attributes_2 = {'Command': 'show ip bgp vrf all', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip bgp (data_2)')
    assert len(result_2) > 1

    # make comparision of two ip ospf neighbor table with index of neighbor ID
    # only find out the ospf state difference
    print('\nIP BGP Table Comparision: index on neighbor NETWORK and compare only NEXT_HOP')
    diff_config = {'index' :['NETWORK'],
                   'check' :['NEXT_HOP'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []

def test_cliparser_show_ip_mfib():
    '''
    Test the 'show ip mfib' command
    '''
    print("\nDoing show ip mfib test!!")

    # test two basic parsing
    data_1 = \
'''
Activity poll time: 60 seconds
  224.0.1.129
    Vlan110
    Cpu
  224.0.1.129 10.30.80.10
    Vlan110 (iif)
      Activity 0:00:12 ago
  224.0.1.129 10.30.80.15
    Vlan110 (iif)
      Activity 0:00:12 ago
  239.194.3.51
    Ethernet37 (iif)
    Vlan590
    Cpu
  239.194.3.51 10.17.12.55
    Ethernet37 (iif)
    Vlan590
      Activity 0:00:12 ago
  239.194.3.52
    Ethernet37 (iif)
    Vlan590
    Cpu
  239.194.3.52 10.17.12.65
    Ethernet37 (iif)
    Vlan590
      Activity 0:00:12 ago
  239.194.3.53
    Ethernet37 (iif)
    Vlan590
    Cpu
  239.194.3.53 10.17.12.75
    Ethernet37 (iif)
    Vlan590
      Activity 0:00:12 ago
  239.194.3.54
    Ethernet37 (iif)
    Vlan590
    Cpu
'''
    attributes_1 = {'Command': 'show ip mfib', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip mfib (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''
Activity poll time: 60 seconds
  224.0.1.129
    Vlan110
    Cpu
  224.0.1.129 10.30.80.10
    Vlan110 (iif)
      Activity 0:00:12 ago
  224.0.1.129 10.30.80.15
    Vlan110 (iif)
      Activity 0:00:12 ago
  239.194.3.51
    Ethernet37 (iif)
    Vlan591
    Cpu
  239.194.3.51 10.17.12.55
    Ethernet37 (iif)
    Vlan590
      Activity 0:00:12 ago
  239.194.3.52 10.17.12.65
    Ethernet37 (iif)
    Vlan590
      Activity 0:00:12 ago
  239.194.3.53
    Ethernet37 (iif)
    Vlan590
    Cpu
  239.194.3.53 10.17.12.75
    Ethernet37 (iif)
    Vlan590
      Activity 0:00:12 ago
  239.194.3.55
    Ethernet37 (iif)
    Vlan590
    Cpu
'''
    attributes_2 = {'Command': 'show ip mfib', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip mfib (data_2)')
    assert len(result_2) > 1

    # make comparision of two ip ospf neighbor table with index of neighbor ID
    # only find out the ospf state difference
    print('\nMFIB Table Comparision: index on neighbor ID and compare only state')
    diff_config = {'index' :['MCAST_GROUP', 'MCAST_SOURCE'],
                   'check' :['INCOMING_INF', 'OUTGOING_INF'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []

def test_cliparser_show_ip_mroute():
    '''
    Test the 'show ip mroute' command
    '''
    print("\nDoing show ip mroute test!!")

    # test two basic parsing
    data_1 = \
'''
PIM Sparse Mode Multicast Routing Table
Flags: E - Entry forwarding on the RPT, J - Joining to the SPT
       R - RPT bit is set, S - SPT bit is set
       W - Wildcard entry, X - External component interest
       I - SG Include Join alert rcvd, P - Ex-Prune alert rcvd
       H - Joining SPT due to policy, D - Joining SPT due to protocol
       Z - Entry marked for deletion
       A - Learned via Anycast RP Router, M - Learned via MSDP
       N - May notify MSDP
RPF route: U - From unicast routing table
           M - From multicast routing table
224.0.1.129
  0.0.0.0/0, 31d07h, RP 10.30.95.1, flags: W
    Incoming interface: register
    RPF route: [U][C] 10.30.95.1/32 [0/1] via 10.30.95.1
    Outgoing interface list:
      Vlan110
  10.30.80.10, 14d10h, flags: SAN
    Incoming interface: Vlan110
    RPF route: [U][C] 10.30.80.0/24 [0/1] via 10.30.80.3
    Outgoing interface list:
  10.30.80.15, 7d21h, flags: SAN
    Incoming interface: Vlan110
    RPF route: [U][C] 10.30.80.0/24 [0/1] via 10.30.80.3
    Outgoing interface list:
239.194.3.51
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.55, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
239.194.3.52
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.65, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
239.194.3.53
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.75, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
239.194.3.54
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.85, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
'''
    attributes_1 = {'Command': 'show ip mroute', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip mroute (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''
PIM Sparse Mode Multicast Routing Table
Flags: E - Entry forwarding on the RPT, J - Joining to the SPT
       R - RPT bit is set, S - SPT bit is set
       W - Wildcard entry, X - External component interest
       I - SG Include Join alert rcvd, P - Ex-Prune alert rcvd
       H - Joining SPT due to policy, D - Joining SPT due to protocol
       Z - Entry marked for deletion
       A - Learned via Anycast RP Router, M - Learned via MSDP
       N - May notify MSDP
RPF route: U - From unicast routing table
           M - From multicast routing table
224.0.1.129
  0.0.0.0/0, 31d07h, RP 10.30.95.1, flags: W
    Incoming interface: register
    RPF route: [U][C] 10.30.95.1/32 [0/1] via 10.30.95.1
    Outgoing interface list:
      Vlan110
  10.30.80.10, 14d10h, flags: SAN
    Incoming interface: Vlan110
    RPF route: [U][C] 10.30.80.0/24 [0/1] via 10.30.80.3
    Outgoing interface list:
  10.30.80.15, 7d21h, flags: SAN
    Incoming interface: Vlan110
    RPF route: [U][C] 10.30.80.0/24 [0/1] via 10.30.80.3
    Outgoing interface list:
239.194.3.51
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.55, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan591
239.194.3.52
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.65, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
239.194.3.53
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
239.194.3.54
  0.0.0.0/0, 10:19:01, RP 10.19.3.1, flags: W
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.19.3.1/32 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
  10.17.12.86, 10:05:58, flags: S
    Incoming interface: Ethernet37
    RPF route: [U][S] 10.17.0.0/17 [1/0] via 10.70.15.73
    Outgoing interface list:
      Vlan590
'''
    attributes_2 = {'Command': 'show ip mroute', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip mroute (data_2)')
    assert len(result_2) > 1

    # make comparision of two ip mroute table with index of neighbor ID
    # only find out the ospf state difference
    print('\nMulticast Routing Table Comparision: index on neighbor ID and compare only state')
    diff_config = {'index' :['MCAST_GROUP', 'MCAST_SOURCE'],
                   'check' :['INCOMING_INF', 'OUTGOING_INF'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []

def test_cliparser_show_ip_ospf_database():
    '''
    Test the 'show ip ospf database' command
    '''
    print("\nDoing show ip ospf database test!!")

    # test two basic parsing
    data_1 = \
'''
            OSPF Router with ID(10.30.95.1) (Process ID 1) (VRF default)


                 Router Link States (Area 0.0.0.0)

Link ID         ADV Router      Age         Seq#         Checksum Link count
10.30.47.1      10.30.47.1      1750        0x80012e97   0xfd72   14
10.30.79.1      10.30.79.1      46          0x8000abbd   0xc0d    15
10.30.79.2      10.30.79.2      42          0x8000abb9   0x35ca   17
10.30.79.5      10.30.79.5      1871        0x80009eb6   0xc64b   3
10.30.47.2      10.30.47.2      17          0x80012e85   0x1298   18
10.30.47.5      10.30.47.5      1077        0x8001188d   0x3d24   5
10.30.63.2      10.30.63.2      1052        0x8000d36b   0x5674   15
10.30.31.9      10.30.31.9      1314        0x8000fb1f   0x534f   10
10.30.31.10     10.30.31.10     1009        0x8000fb1a   0x757d   7
10.30.31.4      10.30.31.4      6           0x80015c88   0x588f   5
10.30.31.6      10.30.31.6      817         0x800162ad   0x5051   9
10.30.31.7      10.30.31.7      149         0x8000f822   0xf769   3
10.30.31.5      10.30.31.5      510         0x80015071   0x4955   8
10.30.31.1      10.30.31.1      357         0x8001a7a0   0x96f5   13
10.30.31.3      10.30.31.3      1232        0x80015ca9   0x63c    12
10.30.95.4      10.30.95.4      355         0x80008b9f   0x920d   6
10.30.95.2      10.30.95.2      712         0x800004ac   0xdff0   13
10.30.95.3      10.30.95.3      1569        0x80008bb0   0xcd0    8
10.30.95.1      10.30.95.1      225         0x8000ac88   0xd5a0   16
10.30.63.1      10.30.63.1      359         0x8000d366   0xaebc   14

                 Type-5 AS External Link States

Link ID         ADV Router      Age         Seq#         Checksum Tag
171.147.239.197 10.30.47.5      1077        0x80004334   0xd29    0
10.201.0.87     10.30.31.1      1557        0x80000a61   0x9fd3   0
170.240.0.0     10.30.47.5      1077        0x800113b4   0x42fe   0
10.66.0.76      10.30.31.1      957         0x80003b3d   0xf7e0   0
10.28.132.128   10.30.47.5      1077        0x800064e3   0x41f4   0
10.16.32.71     10.30.47.5      565         0x8000006e   0xa012   0
10.16.32.74     10.30.47.5      565         0x8000006e   0x822d   0
10.4.92.28      10.30.47.5      565         0x8000006e   0x4a63   0
10.28.134.1     10.30.47.5      1077        0x800064e3   0x505c   0
10.66.0.74      10.30.31.1      957         0x80003b3d   0xcce    0
'''
    attributes_1 = {'Command': 'show ip ospf database', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip ospf database (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''

            OSPF Router with ID(10.30.95.1) (Process ID 1) (VRF default)


                 Router Link States (Area 0.0.0.0)

Link ID         ADV Router      Age         Seq#         Checksum Link count
10.30.47.1      10.30.47.1      1750        0x80012e97   0xfd72   14
10.30.79.1      10.30.79.2      46          0x8000abbd   0xc0d    15
10.30.79.2      10.30.79.2      42          0x8000abb9   0x35ca   17
10.30.79.5      10.30.79.5      1871        0x80009eb6   0xc64b   3
10.30.47.2      10.30.47.2      17          0x80012e85   0x1298   18
10.30.47.5      10.30.47.5      1077        0x8001188d   0x3d24   5
10.30.63.2      10.30.63.2      1052        0x8000d36b   0x5674   15
10.30.31.9      10.30.31.9      1314        0x8000fb1f   0x534f   10
10.30.31.10     10.30.31.10     1009        0x8000fb1a   0x757d   7
10.30.31.4      10.30.31.4      6           0x80015c88   0x588f   5
10.30.31.6      10.30.31.6      817         0x800162ad   0x5051   9
10.30.31.7      10.30.31.7      149         0x8000f822   0xf769   3
10.30.31.5      10.30.31.5      510         0x80015071   0x4955   8
10.30.31.1      10.30.31.1      357         0x8001a7a0   0x96f5   13
10.30.31.3      10.30.31.3      1232        0x80015ca9   0x63c    12
10.30.95.4      10.30.95.4      355         0x80008b9f   0x920d   6
10.30.95.2      10.30.95.2      712         0x800004ac   0xdff0   13
10.30.95.3      10.30.95.3      1569        0x80008bb0   0xcd0    8
10.30.95.1      10.30.95.1      225         0x8000ac88   0xd5a0   16
10.30.63.1      10.30.63.1      359         0x8000d366   0xaebc   14

                 Type-5 AS External Link States

Link ID         ADV Router      Age         Seq#         Checksum Tag
171.147.239.197 10.30.47.5      1077        0x80004334   0xd29    0
10.201.0.87     10.30.31.1      1557        0x80000a61   0x9fd3   0
170.240.0.0     10.30.47.5      1077        0x800113b4   0x42fe   0
10.66.0.76      10.30.31.1      957         0x80003b3d   0xf7e0   0
10.28.132.128   10.30.47.5      1077        0x800064e3   0x41f4   0
10.16.32.71     10.30.47.5      565         0x8000006e   0xa012   0
10.4.92.28      10.30.47.5      565         0x8000006e   0x4a63   0
10.28.134.1     10.30.47.5      1077        0x800064e3   0x505c   0
10.66.0.75      10.30.31.1      957         0x80003b3d   0xcce    0
'''
    attributes_2 = {'Command': 'show ip ospf database', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip ospf database (data_2)')
    assert len(result_2) > 1

    # make comparision of two show ip ospf database table with index of neighbor ID
    # only find out the ospf state difference
    print('\nMulticast Routing Table Comparision: index on neighbor ID and compare only state')
    diff_config = {'index' :['LINK_ID',],
                   'check' :['ADV_ROUTER'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []
def test_cliparser_ip_pim_interface():
    '''
    Test the 'show ip pim interface' command
    '''
    print("\nDoing show ip pim interface test!!")

    # test two basic parsing
    data_1 = \
'''
Address         Interface        Mode       Neighbor   Hello DR         DR Address      PktsQed      PktsDropped
                                            Count      Intvl Pri
10.30.94.5      Ethernet33       sparse     1          30    1          10.30.94.6      0            0
10.70.15.74     Ethernet37       sparse     1          30    1          10.70.15.74     0            0
10.30.80.3      Vlan110          sparse     1          30    100        10.30.80.3      0            6
10.30.94.30     Vlan216          sparse     1          30    1          10.30.94.30     0            4
10.30.94.37     Vlan224          sparse     1          30    1          10.30.94.38     0            0
10.196.101.9    Vlan413          sparse     0          30    1          10.196.101.9    0            0
10.192.114.1    Vlan590          sparse     0          30    1          10.192.114.1    0            0
10.30.94.1      Vlan902          sparse     1          30    1          10.30.94.2      0            0
'''
    attributes_1 = {'Command': 'show ip pim interface', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)
    DiffTable.pretty_table_print(result_1, title='show ip pim interface (data_1)')
    assert len(result_1) > 1

    data_2 = \
'''
Address         Interface        Mode       Neighbor   Hello DR         DR Address      PktsQed      PktsDropped
                                            Count      Intvl Pri
10.30.94.5      Ethernet33       sparse     1          30    1          10.30.94.6      0            0
10.70.15.75     Ethernet37       sparse     1          30    1          10.70.15.74     0            0
10.30.80.3      Vlan110          sparse     1          30    100        10.30.80.3      0            6
10.30.94.30     Vlan216          sparse     1          30    1          10.30.94.30     0            4
10.30.94.37     Vlan224          sparse     1          30    1          10.30.94.38     0            0
10.196.101.9    Vlan413          sparse     0          30    1          10.196.101.9    0            0
10.30.94.1      Vlan902          sparse     1          30    1          10.30.94.2      0            0
'''
    attributes_2 = {'Command': 'show ip pim interface', 'Vendor': 'Arista', 'Version': 'DEFAULT'}
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)
    DiffTable.pretty_table_print(result_2, title='show ip pim interface (data_2)')
    assert len(result_2) > 1

    # make comparision of two show ip pim interface table with index of neighbor ID
    # only find out the ospf state difference
    print('\nPIM Neighbor Table Comparision: index on neighbor ID and compare only state')
    diff_config = {'index' :['ADDRESS', 'INTERFACE'],
                   'check' :[],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    DiffTable.print_diff_entries(diff, print_same=True)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] == []

if __name__ == '__main__':
    test_cliparser_show_ip_route()
    test_cliparser_show_ip_bgp_sum()
    test_cliparser_show_ip_ospf_neighbor()
    test_cliparser_show_interfaces()
    test_cliparser_show_ip_bgp()
    test_cliparser_show_ip_mfib()
    test_cliparser_show_ip_mroute()
    test_cliparser_show_ip_ospf_database()
    test_cliparser_ip_pim_interface()
