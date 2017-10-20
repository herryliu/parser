#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

import pandas as pd
import textfsm
import clitable

TEMPLATE_INDEX_DIR = './template/'
TEMPLATE_INDEX_FILE = 'index'
DEFAULT_ATTRIBUTE = {'Version': 'DEFAULT'}

class CliParser(clitable.CliTable):
    '''
    CliPaser read in an index file in a template directory. Based on attributes defined,
    it will find a match parser template file in the template diretory and use that
    template file to parse the input data. It returns a list for each parsed record.
    '''
    def __init__(self, index_file=TEMPLATE_INDEX_FILE,
                 template_dir=TEMPLATE_INDEX_DIR,
                 attributes=None):
        super(CliParser, self).__init__(index_file, template_dir)
        self.template_dir = template_dir
        self.index_file = index_file
        self.attributes = attributes
        # set Version to 'DEFAULT' if it is not defined
        if 'Version' not in attributes.keys():
            self.attributes['Version'] = 'DEFAULT'
        self.cli_table = clitable.CliTable(self.index_file, self.template_dir)

    def parse_cli(self, data=None):
        '''
        parse data by picking the right template based on attributes
        '''
        # determine the template
        row = self.cli_table.index.GetRowMatch(self.attributes)
        if not row:
            print("Can't find related template")
            return None
        template_file = open(self.template_dir + self.index.index[row][0])
        if data is None:
            print("no data to parse")
            return None
        parser = textfsm.TextFSM(template_file)
        result = parser.ParseText(data)
        header = parser.header
        final_result = [header] + result
        return final_result

    @staticmethod
    def direct_parse_cli(data, template):
        '''
        pasrse the data with provided template file directly whtout go through
        searching for template file
        '''
        if not template:
            print("No template file provided")
            return None
        template_file = open(template)
        if data is None:
            print("no data to parse")
            return None
        parser = textfsm.TextFSM(template_file)
        result = parser.ParseText(data)
        header = parser.header
        final_result = [header] + result
        return final_result

    def set_attribute(self, attributes):
        self.attributes = attributes
        # set Version to 'DEFAULT' if it is not defined
        if 'Version' not in attributes.keys():
            self.attributes['Version'] = 'DEFAULT'

    def set_template_dir(self, directory):
        self.template_dir = directory

    def set_index_file(self, index):
        self.index_file = index

class DiffTable(object):
    '''
    Encapulation class with static methods to diff two tables to find out
    new/missing/changed entries
    '''
    @staticmethod
    def diff_generic(data_1, data_2, diff_conf):
        '''
        The generic diff for two tbales with same format
        '''
        # check if data_1 and data_2 has same format
        if not DiffTable.check_data_format(data_1, data_2, diff_conf):
            return None

        # make index based on fields based on diff_conf
        t1 = pd.DataFrame(data=data_1[1:], columns=data_1[0])
        t2 = pd.DataFrame(data=data_2[1:], columns=data_2[0])

        index = diff_conf['index']
        # grouping the entries to make it all unique to index key
        grouping = index
        if grouping:
            t1_grouped = t1.groupby(grouping)
            t2_grouped = t2.groupby(grouping)
            t1 = t1_grouped.agg(lambda x: tuple(x)).reset_index() # pylint: disable=W0108
            t2 = t2_grouped.agg(lambda x: tuple(x)).reset_index() # pylint: disable=W0108


        # make a outer join to formulate a table with all entreis
        result_table = pd.merge(t1, t2, on=index, how='outer',
                                suffixes=['_L', '_R'], indicator='DIFF_RESULT')

        # diff table convert to a list
        # insert a dummy column name at the front to match the merge operation
        result = [[''] + result_table.columns.tolist()] + result_table.reset_index().values.tolist()

        # save result list slice info for later usage
        result_slice = {}
        result_slice['seq'] = slice(0, 1)
        result_slice['index'] = slice(1, len(index)+1)
        result_slice['left'] = slice(len(index)+1, len(data_1[0])+1)
        result_slice['right'] = slice(len(data_1[0])+1, 2*len(data_1[0])-1)
        result_slice['diff'] = slice(2*len(data_1[0])-1, 2*len(data_1[0]))

        # find out which entry is new / missing / changed
        diff = DiffTable.get_diffs(result, result_slice, diff_conf['check'])
        #pprint.pprint(diff, width=2000)
        return diff

    @staticmethod
    def get_diffs(result, result_slice, check):
        '''
        Process the outer join table and format it into a dictionary with new/missing/changed
        The "check" is a list of fileds for comparision based on
        '''
        diff = {'new': [],
                'missing': [],
                'changed': [],
                'header': result[0][result_slice['index']]+ \
                          [x.rstrip('_L') for x in result[0][result_slice['left']]]
               }

        # the column name is appended with _L or _R for non-index field
        all_column = result[0]
        # find all checking pair index according to column name
        full_index = [(all_column.index(c+'_L'), all_column.index(c+'_R')) for c in check]
        left_index = [x[0] for x in full_index]
        right_index = [x[1] for x in full_index]
        indicator_index = all_column.index('DIFF_RESULT')

        # for each record, indictor_index either be 'left_only', 'right_only' or 'both'
        for r in result[1:]:
            # new entry if 'leff_only'
            if r[indicator_index] == 'left_only':
                diff['new'].append(r[result_slice['index']] + r[result_slice['left']])
                continue
            # missing entry if 'right_only'
            if r[indicator_index] == 'right_only':
                diff['missing'].append(r[result_slice['index']] + r[result_slice['right']])
                continue
            # find out the changes if 'both'
            if r[indicator_index] == 'both':
                left = [r[i] for i in left_index]
                right = [r[i] for i in right_index]
                if left != right:
                    diff['changed'].append({'lef': r[result_slice['left']],
                                            'right': r[result_slice['right']]
                                           })
        return diff

    @staticmethod
    def check_data_format(data_1, data_2, diff_conf):
        '''
        check if two data set has same data format and diff_conf is with right fields
        '''
        # check if the column name has the same content
        if data_1[0] != data_2[0]:
            print('Column Name is not matching for those two data:\n data 1:%s \n data 2: %s' %
                  data_1, data_2)
            return False
        # check if the diff_conf using the right column name
        column_name = data_1[0]
        for conf in diff_conf.values():
            # check if conf is subset of column name
            if not frozenset(conf).issubset(frozenset(column_name)):
                print("diff_conf %s is not in %s" % (conf, column_name))
                return False
        return True
