#!/usr/bin/env python

import pprint
import textfsm

template = open('./arista_eos_show_lldp_neighbors_detail.template')
raw_data = open('./arista_eos_show_lldp_neighbors_detail.data').read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)

#pprint.pprint(data)
for line in data:
    print(line)
