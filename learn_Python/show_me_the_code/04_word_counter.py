# !/usr/bin/python
# encoding: utf-8
# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

from collections import Counter
import re

FILE_NAME = r'D:\developer\others\1\static\README.md'

def count_word(the_string):
    word_list = re.findall(r"[\w']+", the_string)
    word_dic = Counter(word_list)
    return word_dic

def merge_dics(old_dict, new_dict):
    for k, v in new_dict.iteritems():
        if k in old_dict:
            old_dict[k] = old_dict[k] + v
        else:
            old_dict[k] = v

    return old_dict

def count_word_from_file(file_name):
    with open(file_name, 'r+') as open_file:
        old_dict = {}
        for line in open_file:
            new_dict = count_word(line)
            old_dict = merge_dics(new_dict, old_dict)

        open_file.close()
        return len(new_dict)

if __name__ == '__main__':


    print count_word_from_file(FILE_NAME)

    # a = {'a':1, 'b':2}
    # b = {'b':3, 'c':4}

    # a = 'a b, c '
    # print count_word(a)