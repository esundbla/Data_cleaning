import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np





def green_extract(rgb):
    mod = rgb
    length, width, extra = rgb.shape
    grn_pix_count = 0
    for i in range(length):
        for j in range(width):
            if (mod[i, j, 0] < 125 and mod[i, j, 0] > 50) and mod[i, j, 1] > 135 and (mod[i, j, 2] > 80 and mod[i, j, 2] < 165):
                grn_pix_count += 1
            else:
                mod[i, j, :] = 0

    return mod, grn_pix_count


if __name__ == "__main__":
    src = cv.imread('S008/06-05-2019/104403.JPG')
    rgb = cv.cvtColor(src, cv.COLOR_BGR2RGB)
    plt.figure()
    plt.title('original')
    plt.imshow(src)
    mod, grn_pix_count = green_extract(src)
    plt.figure()
    plt.title("mod")
    plt.imshow(mod)
    plt.show()
    print(grn_pix_count)
