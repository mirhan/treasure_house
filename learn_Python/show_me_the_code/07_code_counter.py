# !/usr/bin/python
# encoding: utf-8
# 第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

FILE_DIR = r"D:\developer\treasure_house\trunk\learn_Python\show_me_the_code"

import os

def get_first_letter(line):
    for letter in line:
        if letter.isspace():
            continue
        else:
            return letter
    return None

def file_counter(filename):
    f_counter = {'empty_line':0, 'comment':0, 'code':0}
    if not os.path.isfile(filename):
        return f_counter

    with open(filename, 'r+') as open_file:
        for line in open_file:
            first_letter = get_first_letter(line)
            if None == first_letter:
                f_counter['empty_line'] = f_counter['empty_line'] + 1
            elif'#' == first_letter:
                f_counter['comment'] = f_counter['comment'] + 1
            else:
                f_counter['code'] = f_counter['code'] + 1

    open_file.close()
    return f_counter

def file_counter_from_dir(file_dir):
    d_counter = {}
    if not os.path.isdir(file_dir):
        return d_counter

    for f in os.listdir(file_dir):
        f_path = os.path.join(file_dir, f)
        d_counter[f] = file_counter(f_path)

    return d_counter

if __name__ == '__main__':
    print file_counter_from_dir(FILE_DIR)