# encoding: utf-8
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

import string

FILTER_WORDS_PATH = r'D:\developer\treasure_house\trunk\learn_Python\show_me_the_code\11_filtered_words.txt'

def get_filter_words(filter_words_path):
    open_file = open(filter_words_path, 'r+').readlines()

    for i in range(len(open_file)):
        open_file[i] = open_file[i].strip()

    return open_file

def is_string_banned(s):
    is_banned = False
    filter_words = get_filter_words(FILTER_WORDS_PATH)
    for filter_word in filter_words:
        if filter_word in s:
            is_banned = True
            break

    return is_banned

if __name__ == '__main__':
    while 1:
        name_yo = raw_input('Enter a name: ')
        print name_yo, is_string_banned(name_yo)
