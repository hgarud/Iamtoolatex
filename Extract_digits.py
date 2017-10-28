# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:35:25 2017

@author: NIRMAL ELAMON
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:19:37 2017

@author: NIRMAL ELAMON
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:55:55 2017

@author: NIRMAL ELAMON
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:44:19 2017

@author: NIRMAL ELAMON
"""

import cv2
import numpy as np
import imutils
from imutils import contours
x='F:\\masters\\data science\\individual project\\codes\\formula.jpg'
img=cv2.imread(x,0)
img = cv2.bitwise_not(img)
th,dst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)



cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

c=[]
x1,x2=dst.shape

for i in range(x1):
    for j in range(x2):
        if dst[i][j]==255:
          c.append([[i],[j]])
[l1,l2,l3]=np.shape(c) 
c=np.array(c) 
x_min=np.amin(c[:,0])
x_max=np.amax(c[:,0])
y_min=np.amin(c[:,1])
y_max=np.amax(c[:,1])

crop_image=img[(x_min-1):(x_max+1),(y_min-1):(y_max+1)]
cv2.imshow('crop',crop_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


cnts = cv2.findContours(dst, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if imutils.is_cv2() else cnts[1]
digitCnts = sorted(cnts, key=cv2.contourArea, reverse=True)


    

digitCnts = contours.sort_contours(digitCnts,method="left-to-right")[0]
digits = []

for c in digitCnts:
	
    (x, y, w, h) = cv2.boundingRect(c)
    roi = dst[y:y + h, x:x + w]
    cv2.imshow('image',roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
