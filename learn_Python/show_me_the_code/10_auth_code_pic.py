# !/usr/bin/python
# encoding: utf-8
# 第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

import string
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter

def random_auth_code(sample_len):
    return ''.join(random.sample(string.ascii_letters + string.digits, sample_len))

def random_color():
    return (random.randint(50,200),random.randint(50,200),random.randint(50,200))

def auth_code_to_pic(auth_code, width = 400, height = 200):
    font = ImageFont.truetype('verdana.ttf', width / len(auth_code)) # unconfirmed
    font_width, font_height = font.getsize(auth_code)

    im = Image.new('RGB', (width, height ), (255,255,255))
    draw = ImageDraw.Draw(im)
    y = (height - font_height) / 2
    margin_width = (width - font_width) / (len(auth_code) + 1)

    # draw auth code
    x = margin_width
    for i, v in enumerate(auth_code):
        draw.text((x, y), v, random_color(), font)
        x = x + margin_width + font_width / len(auth_code)

    # draw noise
    for x in range(width):
        for y in range(height):
            color = im.getpixel((x, y))
            if (color == (255, 255, 255)):
                draw.point((x, y), fill = random_color())
            elif random.random() > 0.618:
                draw.point((x, y), fill = random_color())

    im = im.filter(ImageFilter.BLUR)
    im.show()

if __name__ == '__main__':
    auth_code_to_pic(random_auth_code(4))