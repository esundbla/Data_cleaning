import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os


def pixel_counter(img, len, wid):
    total = len * wid
    for i in range(len):
        for j in range(wid):
            if img[i,j,2] >


if __name__=="__main__":
    directory = 'S008'
    sample = open((directory+'0'), "w")
    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        for images in os.listdir(f):
            image = os.path.join(f, images)
            photo = cv.imread(image)
            length, width, extra = photo.shape
            rgb = cv.cvtColor(photo, cv.COLOR_BGR2RGB)
            green_pixel_percent = pixel_counter(rgb, length, width)

    exit(0)