import cv2 as cv
import numpy as np

if __name__=="__main__":
    img = cv.imread('NonReal.JPG')
    try:
        length, width, extra = img.shape
    except:
        print("caught it")

    print("Didn't Die!")