import cv2
import numpy as np
import glob
import os
import re

print("hi")
ip_location = "D:\\1Hrishi\\NC State\\1 Study\\3 Topics in Data Science\\Project\\Independent Project\\formula_images\\"
#op_location = "D:\\1Hrishi\\NC State\\1 Study\\3 Topics in Data Science\\Project\\Independent Project\\resized_formula_images\\"
image_ext = "*.png"
image_list = glob.glob(ip_location + image_ext)
image_count = 2
image_padding = 1
#print(image_list)
for image_name in image_list[0:1]:
    #print(image_name)
    image = cv2.imread(image_name)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', image)
    indices = np.where(gray_image == gray_image.min())
    formula_image = gray_image[indices[0].min()-image_padding:indices[0].max()+image_padding,
									indices[1].min()-image_padding:indices[1].max()+image_padding]
    resized_formula_image = cv2.resize(formula_image, (28,28))
    height, width = formula_image.shape
    #print(height, width)
    height1, width1 = resized_formula_image.shape
    #print(height1, width1)
    #cv2.imshow('formula_image', formula_image)
    #cv2.imshow('resized_formula_image', formula_image)
    name = re.findall('formula_images\\\([0-9].*).png', image_name)
    #print(name)
    temp = os.path.join(op_location ,str(name)+".png")
    #print(temp)
    cv2.imwrite(temp, resized_formula_image)
    cv2.waitKey(0)
    
