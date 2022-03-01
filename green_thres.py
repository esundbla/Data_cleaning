import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


if __name__=="__main__":
    src = cv.imread('S008/06-05-2019/104403.JPG')
    rgb = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(rgb, cv.COLOR_RGB2HSV)
    plt.figure()
    plt.title('hsv')
    plt.imshow(hsv)
    plt.figure()
    plt.title('original')
    plt.imshow(rgb)
    mod = rgb
    length, width, extra = rgb.shape
    grn_pix_count = 0
    for i in range(length):
        for j in range(width):
            if rgb[i,j,2] > 145:
                mod[i, j, :] = 0
            if mod[i, j, 0] > 100 and mod[i, j, 1]  > 100 and mod[i, j, 2] > 70:
                grn_pix_count += 1
    plt.figure()
    plt.title("mod")
    plt.imshow(mod)
    plt.show()
    print(grn_pix_count)
