#!/usr/bin/env python
# -*- coding: utf-8 -*

"""
Read pictures from a file, change it to resolution 344*344, and save them in a new file
New pictures' name is the same as before

PIL is only used for python 2, so we install pillow instead
Image packet should be installed

This code works on Pycharm
"""

import os
import glob
from PIL import Image

img_path = glob.glob("D:/UF/dataset-2019 microstructure/picture/*.png")
path_save = "D:/UF/dataset-2019 microstructure/sizechangtest/after"

for file in img_path:

    im = Image.open(file)
    new_image = im.resize((344,344))

    print(new_image.format, new_image.size, new_image.mode)
    new_image.save(os.path.join(path_save, os.path.basename(file)))

