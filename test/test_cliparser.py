#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

import pprint

from systemslib.net.parser.cliparser import CliParser, DiffTable

def test_cliparser_show_ip_bgp_sum():
    '''
    Test the 'show ip bgp summary' command
    '''
    print("Doing show ip bgp sum test!!")

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
    assert len(result_1) > 1
    pprint.pprint(result_1)

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
    assert len(result_2) > 1
    pprint.pprint(result_2)

    # make comparision of two BGP table with index of BGP neighbor and AS number
    # only find out the bgp state difference
    diff_config = {'index' :['BGP_NEIGH', 'NEIGH_AS'],
                   'check' :['STATE'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] == []
    pprint.pprint(diff)

    # make comparision of two BGP table with index of BGP neighbor and AS number
    # find out difference in recieved and published route
    diff_config = {'index' :['BGP_NEIGH', 'NEIGH_AS'],
                   'check' :['STATE_PFXRCD', 'STATE_PFXACC'],
                  }
    diff = DiffTable.diff_generic(result_1, result_2, diff_config)
    assert diff['missing'] != []
    assert diff['new'] != []
    assert diff['changed'] != []
    pprint.pprint(diff)

    # test direct parser with supplied template file and
    # should have same parse result as first one
    result_3 = CliParser.direct_parse_cli(data_1,
                                          './template/arista_eos_show_ip_bgp_summary.template')
    assert result_1 == result_3
    pprint.pprint(result_3)

    # test different version
    attributes_4 = {'Command': 'show ip bgp summary', 'Vendor': 'Arista', 'Version': 'V1'}
    parser = CliParser(attributes=attributes_4)
    result_4 = parser.parse_cli(data=data_1)
    assert len(result_4) > 1
    pprint.pprint(result_4)
