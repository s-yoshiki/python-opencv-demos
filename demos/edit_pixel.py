import cv2
import numpy as np 

#img = cv2.imread('lena.png')
img = cv2.imread("./lena.png")

for i in range(512):
	for j in range(512):
		pix = img[i][j]
		th = pix[0]/3.0+pix[1]/3.0+pix[2]/3.0
		pix[0] = 255
		pix[1] = th*0.8
		pix[2] = th*0.8
		img[i][j] = pix

cv2.namedWindow('edge')
cv2.imshow('edge', img)
#cv2.imwrite("el2.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

exit()	
