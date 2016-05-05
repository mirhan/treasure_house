# !/usr/bin/python
# encoding: utf-8
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）

import string
import random

CODE_COUNT = 20
CODE_LEN = 6

def make_auth_code(code_len):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(code_len))

if __name__ == '__main__':
    for i in range(CODE_COUNT):
        print i, make_auth_code(CODE_LEN)