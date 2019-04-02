import numpy as np
import cv2

#  像这种只能表示的是多维数组里面的某一个点的值，可想象成某一个点的权重值
# a = np.array([[[1,2],[3,4]]])
# print(a)
# print(type(a))
# print(a.size)
# print(a.shape)

img = cv2.imread("/Users/shucan/Desktop/111.PNG",0)

print(img)

print(img.shape)