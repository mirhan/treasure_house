# encoding: utf-8
# 第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

import string

FILTER_WORDS_PATH = r'D:\developer\treasure_house\trunk\learn_Python\show_me_the_code\11_filtered_words.txt'
YOU_KNOW_LETTER = '*'

def get_filter_words(filter_words_path):
    open_file = open(filter_words_path, 'r+').readlines()

    for i in range(len(open_file)):
        open_file[i] = open_file[i].strip()

    return set(open_file)

def is_string_banned(s):
    is_banned = False
    filter_words = get_filter_words(FILTER_WORDS_PATH)
    filter_word = ''
    for filter_word in filter_words:
        if filter_word in s:
            is_banned = True
            break

    return is_banned, filter_word

if __name__ == '__main__':
    while 1:
        name_yo = raw_input('Enter a name: ')
        is_banned, filter_word = is_string_banned(name_yo)
        if is_banned:
            new_name = name_yo.replace(filter_word, YOU_KNOW_LETTER * len(filter_word))

        print new_name