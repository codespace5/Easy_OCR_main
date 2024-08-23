import cv2
import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img  = cv2.imread('ocr1.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

d11 = pytesseract.image_to_string(gray_img)

print("12", str(d11))
