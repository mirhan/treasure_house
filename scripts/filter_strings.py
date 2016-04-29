#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
import re

log_path = r"D:\userdata\chanhan\Desktop\tmp\2016-2-1_trace_log_miss_log\log\NG0000351942302.tar\NG0000351942302_syslog-AS7-0.log"
filter_str = r'''session_ctrl_2[4471]'''
filter_str_2 = r'''TRANSACTION'''

def make_new_file_path(old_path):
    return 'one_more_time.log'
    # return old_path + "_filter_" + filter_str + '.log'

if __name__ == '__main__':
    new_fp = open(make_new_file_path(log_path), 'w')
    with open(log_path, 'r+') as openfileobject:
        for line in openfileobject:
            if filter_str in line and filter_str_2 in line:
                new_fp.write(line)

    new_fp.flush()






