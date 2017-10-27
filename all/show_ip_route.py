#!/usr/bin/env python

import pprint
import textfsm

template = open('./arista_eos_show_ip_route.template')
raw_data = open('./arista_eos_show_ip_route.data').read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_data)

#pprint.pprint(data)
for line in data:
    print(line)
