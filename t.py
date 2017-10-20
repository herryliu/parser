#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

import pprint

from cliparser import *

if __name__ == '__main__':

    attributes_1 = {'Command': 'show ip bgp summary', 'Vendor': 'Arista'}
    data_1 = '''BGP summary information for VRF default
Router identifier 10.30.95.2, local AS number 65200
Neighbor         V  AS      MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
10.30.31.3       4  65200   8091068   7454502    0    0  170d15h Estab  48     48
10.30.47.1       4  65200   7467159   7454575    0    0  862d16h Estab  46     46
10.30.94.34      4  65202   4765404   3668243    0    0   13d16h Estab  5      5
'''
    parser = CliParser(attributes=attributes_1)
    result_1 = parser.parse_cli(data=data_1)

    attributes_2 = {'Command': 'show ip bgp summary', 'Vendor': 'Arista'}
    data_2 = '''BGP summary information for VRF default
Router identifier 10.30.95.2, local AS number 65200
Neighbor         V  AS      MsgRcvd   MsgSent  InQ OutQ  Up/Down State  PfxRcd PfxAcc
10.30.31.3       4  65200   8091068   7454502    0    0  170d15h Estab  48     48
10.30.47.2       4  65200   7467159   7454575    0    0  862d16h Estab  46     46
10.30.94.34      4  65202   4765404   3668243    0    0   13d16h Estab  5      6
'''
    parser = CliParser(attributes=attributes_2)
    result_2 = parser.parse_cli(data=data_2)

    diff_config = {
             'index' :['BGP_NEIGH', 'NEIGH_AS'],
             #'check' :['STATE'],
             'check' :['STATE_PFXRCD', 'STATE_PFXACC'],
            }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    pprint.pprint(diff)

    print(CliParser.direct_parse_cli(data_1, './template/arista_eos_show_ip_bgp_summary.template'))
