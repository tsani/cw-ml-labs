#!/usr/bin/env python

from PIL import Image

import csv
import os
import os.path as path
import sys

def extract_image_color(im):
    im.convert(mode='RGB')
    return im.getpixel((0, 0))[:3]

def extract_all_images_colors(subdir):
    return [
        extract_image_color(Image.open(path.join(subdir, image_name)))
        for image_name
        in os.listdir(subdir)
    ]

def process_training_data(root):
    return {
        color_name: extract_all_images_colors(path.join(root, color_name))
        for color_name
        in os.listdir(root)
    }

def main():
    root = path.join('KNN_color_recognition', 'training_dataset')

    colors = process_training_data(root)
    writer = csv.writer(sys.stdout)

    writer.writerow(['color name', 'red', 'green', 'blue'])
    for color_name, color_values in colors.items():
        for rgb in color_values:
            if type(rgb) == int:
                continue # fucky
            writer.writerow([color_name] + list(rgb))
    sys.stdout.close()

if __name__ == '__main__':
    main()
