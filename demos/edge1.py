import cv2
import numpy as np 
import sys

cv2.namedWindow('edge')
img = cv2.imread('lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thrs1 =1000
thrs2 =10
edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
cv2.imshow('edge', edge)

cv2.waitKey(0)
cv2.destroyAllWindows()

exit()	
