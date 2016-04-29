#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
import re

file_path = r"D:\userdata\chanhan\Desktop\code_store\1.log"

if __name__ == '__main__':
    new_fp = open(file_path, 'w')
    for i, v in enumerate(range(0, 100)):
        new_fp.write(str(i) + '\n')

    new_fp.flush()






