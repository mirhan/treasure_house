#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string
import re
import threading
import random
import os
import time

# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log\photos_100_' + str(cid) + '.log')
log_path = '/mnt/developer/hot-samer_mirhan/trunk/same_spider/log/photos_100_1_2.log'
pic_path = '/home/chanhan/Pictures'

def make_new_file_path(old_path):
    return 'one_more_time.log'
    # return old_path + "_filter_" + filter_str + '.log'

def download_url(_to, _from):
    if _to == None or _from == None:
        print 'error, _to = %s, _from = %s' % _to, _from
    else:
        _cmd = 'wget -P %s %s' % (_to, _from)
        os.system(_cmd)

if __name__ == '__main__':
    with open(log_path, 'r+') as openfileobject:
        i = 0
        threads = []
        for line in openfileobject:
            line = line.rstrip()
            # download_url(pic_path, line)
            print pic_path
            print line
            a = threading.Thread(target=download_url,args=(pic_path, line))
            threads.append(a)
            a.start()

            i = i + 1
            if i % 10 == 0:
                print i
            time.sleep(random.random())

        for x in threads:
            x.join()








