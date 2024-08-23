import cv2
import os,argparse
import pytesseract
from PIL import Image
import numpy as np 
#We then Construct an Argument Parser

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#We then read the image with text
images=cv2.imread('ocr1.jpg')
 
#convert to grayscale image
gray=cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
 
#checking whether thresh or blur
cv2.threshold(gray, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1]
cv2.medianBlur(gray, 3)

lower = np.array([200, 200, 200], dtype='uint8')
upper = np.arange([235, 235, 235], dtype='uint8')
mask  = cv2.inRange(gray, lower,  upper)

color_detect = cv2.bitwise_and(gray, gray, mask=mask)

cv2.imshow('gray', gray)
cv2.imshow('color', color_detect)     
cv2.waitKey(0)
# #memory usage with image i.e. adding image to memory
# text = pytesseract.image_to_string(gray)
# print("text", text)
 
# # show the output images
# cv2.imshow("Image Input", images)
# cv2.imshow("Output In Grayscale", gray)
# cv2.waitKey(0)