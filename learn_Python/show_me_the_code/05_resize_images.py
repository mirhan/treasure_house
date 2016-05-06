# !/usr/bin/python
# encoding: utf-8
# 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

IMAGE_DIR = r'D:\userdata\chanhan\My Documents\My Pictures\wallpapers'

IPHONE5_WIDTH = 640
IPHONE5_HEIGHT = 1366

import os
from PIL import Image

def get_new_size(old_width, old_height):
    ratio = min(IPHONE5_WIDTH / float(old_width), IPHONE5_HEIGHT / float(old_height))
    return old_width * ratio, old_height * ratio

def resize_image(old_image, new_image):
    im = Image.open(old_image)
    new_width, new_hight = get_new_size(*im.size)
    im.thumbnail((new_width, new_hight), Image.ANTIALIAS)

    im.save(new_image)
    # im.show()

def make_new_filename(old_filename):
    if not os.path.isfile(old_filename):
        return

    filename, file_extension = os.path.splitext(old_filename)
    return filename + '_ip5_' + file_extension


def resize_image_in_dir(dirctory_path):
    for f in os.listdir(dirctory_path):
        f_path = os.path.join(dirctory_path, f)
        if os.path.isfile(f_path):
            resize_image(f_path, make_new_filename(f_path))

if __name__ == '__main__':
    resize_image_in_dir(IMAGE_DIR)