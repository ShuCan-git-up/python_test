import cv2
import numpy as np

def rgb2gray_mean(img):
    ratio = 1/3
    init_img = img.astype(np.int32)
    result = ratio * (init_img[...,0] + init_img[...,1] + init_img[...,2])
    return result.astype(np.uint8)

def main():
    color = cv2.imread("/Users/shucan/Desktop/111.PNG")
    print(color.shape)
    gray = rgb2gray_mean(color)
    print(gray.shape)
    cv2.imshow("color", color)
    print(color)
    print(gray)
    # cv2.imshow("gray", gray)
    # cv2.waitkey(0)

print(__name__)
if __name__ == 'builtins':
    print(__name__)
    main()