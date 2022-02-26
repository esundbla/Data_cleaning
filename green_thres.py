import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


if __name__=="__main__":
    src = cv.imread('S008/06-12-2019/325803.JPG')
    rgb = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    plt.figure()
    plt.title('original')
    plt.imshow(rgb)
    mod = rgb
    length, width, extra = rgb.shape
    for i in range(length):
        for j in range(width):
            if rgb[i,j,2] > 145:
                mod[i, j, :] = 0
    plt.figure()
    plt.title("mod")
    plt.imshow(mod)
    plt.show()
