import cv2,numpy as np
img=cv2.imread('image.png',0)
cv2.imshow('Open',cv2.morphologyEx(img,cv2.MORPH_OPEN,np.ones((5,5),np.uint8)));cv2.waitKey(0)
