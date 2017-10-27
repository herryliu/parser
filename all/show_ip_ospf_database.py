#!/usr/bin/env python

import pprint
import textfsm

template = open('./arista_eos_show_ip_ospf_database.template')
raw_data = open('./arista_eos_show_ip_ospf_database.data').read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)

#pprint.pprint(data)
for line in data:
    print(line)
