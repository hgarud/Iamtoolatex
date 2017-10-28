import numpy as np
import cv2
import glob

ip_location = "D:\\1Hrishi\\NC State\\1 Study\\3 Topics in Data Science\\Project\\Independent Project\\formula_images\\"
image_ext = "*.png"
image_list = glob.glob(ip_location + image_ext)
image_count = 2
for image_name in image_list[0:1]:
    im = 255 - cv2.imread(image_name)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('bleh', imgray)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    #im3 = np.ones(im2.shape)
    cnt=contours[2]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(im2,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Show",im2)
    cv2.drawContours(im2, contours, 3, (0,255,0), 3)
    cv2.imshow('meh', im2)
    cv2.waitKey()