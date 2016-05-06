# !/usr/bin/python
# encoding: utf-8
# 第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
# 请将上述内容写到 student.xls 文件中，如下图所示：


# coppied from https://github.com/Show-Me-the-Code/python/blob/master/Forec/0014/0014.py

import xlwt
import re

book = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
sheet = book.add_sheet('student',cell_overwrite_ok = True)
line = 0
info = re.compile(r'\"(\d+)\":\[\"(.*?)\",(\d+),(\d+),(\d+)\]')
with open('student.txt',"r") as f:
    data = f.read()
for x in info.findall(data):
    for i in range(len(x)):
        sheet.write(line,i,x[i])
    line+=1
book.save('student.xls')