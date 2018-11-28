# DIP Projectimport
# Aishwarya Milind Pawar 2015BCS003
# Sukhada Vijay Ghewari 2015BCS016
# Guided by Dr.S.H. Bhandari
# Problem Statement: The hand gestures are to be recognized to build an application.
# Given images of hand gestures, implement suitable segmentation algorithm to detect hand.
import cv2            #importing opencv
import numpy as np    #importing numpy
import math           #importing math library


#function to convert RGB pixel value to YCbCr colour space
def _ycc(r, g, b): 
    y = .299*r + .587*g + .114*b
    cb = 128 -.168736*r -.331364*g + .5*b
    cr = 128 +.5*r - .418688*g - .081312*b
    return y, cb, cr


#function which takes in given .bmp image and displays binarized image with hand detected
def recogHand(hand):
    cv2.imshow('image',hand)   #display original image
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imgYCC = cv2.cvtColor(hand, cv2.COLOR_BGR2YCR_CB)   #convert RGB image to YCbCr colour space
    
    y,cb,cr = _ycc(173,180,242)    #convert defined skin color (in rgb) to YCbCr
    avg_skin_color=[y,cb,cr]

    error = 45  #thresholding value for skin color detection; optimum value found by trial and error


    for i in range(0,240):       #looping through the rows( height)
        for j in range(0,320):   #looping through the columns(width)
            #calculate the Euclidean distance between a pixel and the skin color defined above
            if(math.sqrt((int(imgYCC[i,j,0])- avg_skin_color[0])**2 + (int(imgYCC[i,j,1])- avg_skin_color[1])**2 + (int(imgYCC[i,j,2])- avg_skin_color[2])**2) <= error):    
                    imgYCC[i,j]=[255,255,255]        #make the pixel white
            else:
                imgYCC[i,j]=[0,0,0]                  #make the pixel black
    
    cv2.imshow("hand segmented",imgYCC)              #display final binarized image 
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#loop through all sample images 
for i in range(1,5):
    fname= 'frame'+str(i)+'.bmp'
    hand = cv2.imread(fname,-1)  # -1 indicates reading the image in original color scheme
    recogHand(hand)

