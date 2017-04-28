# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 10:11:42 2017

@author: vishnu.sk
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.ion()


def img_transformation(src_corners,out_corners,image):
    quad_mat, mask = cv2.findHomography(src_corners, out_corners)
    output_ = cv2.warpPerspective(image, quad_mat, (1500,800))
    return output_


def create_test_image(c1,c2):
    mask = np.zeros((500,600, 3), np.uint8)
    cv2.rectangle(mask, c1, c2, (255,0,0), -1)
    return mask


def put_text(img,a,b,c,d):
    cv2.putText(img,'A', tuple(a), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
    cv2.putText(img,'B', tuple(b), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
    cv2.putText(img,'C', tuple(c), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
    d[1] = d[1] + 60
    cv2.putText(img,'D', tuple(d), cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
    return img
    
    
if __name__ == '__main__':
    a_cord = [141,276]
    b_cord = [503,276]
    c_cord = [503,417]
    d_cord = [141,417]
    src_corners = np.float32([a_cord, b_cord, c_cord, d_cord])
    out_corners = np.float32([[955,198], [1071,506], [847,504], [717,281]])
    x1 = min(src_corners[:,0])
    x2 = max(src_corners[:,0])
    y1 = min(src_corners[:,1])
    y2 = max(src_corners[:,1])
    image_ = create_test_image((x1,y1),(x2,y2))
    image_ = put_text(image_, a_cord, b_cord, c_cord, d_cord)
    img_t = img_transformation(src_corners,out_corners,image_)
    plt.imshow(image_)
    plt.title('Input Image')
    plt.figure()
    plt.imshow(img_t)
    plt.title('Output Image') 