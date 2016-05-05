# !/usr/bin/python
# encoding: utf-8
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果

from PIL import Image, ImageDraw, ImageFont

TXT = '9'
NEW_SIZE = (10,10)
ORINGINAL_PIC = r"D:\developer\treasure_house\trunk\learn_Python\pic_to_ascii\ascii_dora.png"

def add_num(picPath, num):
    img = Image.open(picPath)
    x, y = img.size
    myfont = ImageFont.truetype('ahronbd.ttf', x / 3)
    ImageDraw.Draw(img).text((2 * x / 3, 0), str(num), font = myfont,  fill = 'red')
    img.save('pic_with_num.png')
    # img.show()

if __name__ == '__main__':
    add_num(ORINGINAL_PIC, 9)


# if __name__ == '__main__':
#     # get an image
#     base = Image.open(ORINGINAL_PIC).convert('RGBA')

#     # make a blank image for the text, initialized to transparent text color
#     # txt = Image.new('RGBA', base.size, (255,255,255,0))

#     x, y = base.size
#     # get a drawing context
#     d = ImageDraw.Draw(base)

#     # draw text, half opacity
#     myfont = ImageFont.truetype('ahronbd.ttf', x / 3)
#     d.text((2 * x / 3, 0), TXT, font = myfont, fill='red')

#     # out = Image.alpha_composite(base, txt)

#     base.show()
#     # d.show()
